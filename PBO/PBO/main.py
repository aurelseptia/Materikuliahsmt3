from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import mysql.connector

class InputForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Inisialisasi koneksi database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kripik21"
        )
        self.mycursor = self.mydb.cursor()

        # Menyimpan data yang akan diupdate
        self.update_id = None
                # Layout untuk menampilkan data

    def show_data(self):
        try:
        # Ambil data dari text input
        
            nama = self.ids.nama_input.text
            pesanan = self.ids.pesanan_input.text

            # Validasi inputan tidak kosong
            if not nama or not pesanan:
                popup = Popup(
                    title="Error", 
                    content=Label(text="Semua field harus diisi."),
                    size_hint=(0.8, 0.4),
                    auto_dismiss=True
                )
                popup.open()
                return

            # Insert data ke database
            sql = "INSERT INTO tbl_kripik21 (nama, pesanan) VALUES (%s, %s)"
            val = (nama, pesanan)
            try:
                self.mycursor.execute(sql, val)
                self.mydb.commit()
            except Exception as e:
                popup = Popup(
                    title="Database Error",
                    content=Label(text=f"Error: {e}"),
                    size_hint=(0.8, 0.4),
                    auto_dismiss=True
                )
                popup.open()
                return

            # Reset form menjadi kosong
            self.ids.nama_input.text = ""
            self.ids.pesanan_input.text = ""
            self.show_table()
        except Exception as e:
            popup = Popup(
            title="Error",
            content=Label(text=f"Error: {e}"),
            size_hint=(0.8, 0.4),
            auto_dismiss=True
        )
            popup.open()

    def show_table(self):
        # Ambil data dari database
        self.mycursor.execute("SELECT * FROM tbl_kripik21 order by no")
        data_pesanan = self.mycursor.fetchall()

        # Hapus widget di tabel sebelumnya
        self.ids.tabel_pesanan.clear_widgets()

        # Tambahkan header kolom, termasuk kolom Aksi
        self.ids.tabel_pesanan.add_widget(Label(text="Nama", bold=True, size_hint_x=None, width=120, color=(0, 0, 0, 1)))
        self.ids.tabel_pesanan.add_widget(Label(text="Pesanan", bold=True, size_hint_x=None, width=80, color=(0, 0, 0, 1)))

        # Tambahkan header kolom Aksi ke dalam tabel
        self.ids.tabel_pesanan.add_widget(Label(text="Aksi", bold=True, size_hint_x=None, width=50, color=(0, 0, 0, 1)))
        self.ids.tabel_pesanan.add_widget(Label(text="", bold=True, size_hint_x=None, width=50, color=(0, 0, 0, 1)))  # Kolom Aksi


        # Tambahkan data ke tabel
        for index, row in enumerate(data_pesanan, start=1):
            # Kolom No
            self.ids.tabel_pesanan.add_widget(Label(text=str(index), size_hint_x=None, width=40, color=(0, 0, 0, 1)))
            # Kolom Nama
            self.ids.tabel_pesanan.add_widget(Label(text=row[0], size_hint_x=None, width=120, color=(0, 0, 0, 1)))
            # Kolom Pesanan
            self.ids.tabel_pesanan.add_widget(Label(text=row[1], size_hint_x=None, width=80, color=(0, 0, 0, 1)))
    
            # Tambahkan Tombol Delete di kolom aksi di dalam tabel masuk for loop agar tampil disetiap baris data 
            delete_btn = Button(text="DELETE", size_hint_x=None, width=50, font_size=10)
            delete_btn.bind(on_release=lambda btn, row=row: self.delete_data(row[1])) 
            self.ids.tabel_pesanan.add_widget(delete_btn)

            # Tambah Tombol Update di kolom aksi
            update_btn = Button(text="UPDATE", size_hint_x=None, width=50, font_size=10)
            update_btn.bind(on_release=lambda btn, row=row: self.update_data(row[1])) 
            self.ids.tabel_pesanan.add_widget(update_btn)


            

    def update_data(self, pesanan):
        try:
            # Ambil data dari database berdasarkan ID
            query = "SELECT nama, pesanan FROM tbl_pesanan WHERE pesanan = %s"
            self.mycursor.execute(query, (pesanan,))
            result = self.mycursor.fetchone()
            
            if result:
                # Jika data ditemukan, tampilkan di form input
                self.ids.nama_input.text = result[0]  # Nama
                self.ids.pesanan_input.text = result[1]   # Pesanan
                
                # Simpan ID mahasiswa yang akan diupdate
                self.id_update = kripik21
                
                # Ganti teks tombol dari "Tambah Data" menjadi "Update Data"
                self.ids.tombol_simpan.text = "Update Data"
                
                #Membuat input text pesanan tidak bisa diedit
                self.ids.pesanan_input.readonly = True

                # Bind ulang tombol ke fungsi update_data_submit
                self.ids.tombol_simpan.unbind(on_release=self.show_data)
                self.ids.tombol_simpan.bind(on_release=self.update_data_submit)
            else:
                self.show_error_popup("Data tidak ditemukan")
        except Exception as e:
            self.show_error_popup(f"Gagal mengambil data: {e}")



    def update_data_submit(self, instance):
        try:
            # Ambil data dari input form
            nama = self.ids.nama_input.text
            pesanan = self.ids.pesanan_input.text
            # Validasi input form
            if not nama or not pesanan:
                self.show_error_popup("Semua kolom harus diisi!")
                return
            # Query untuk mengupdate data pesanan
            query = "UPDATE tbl_pesanan SET nama = %s, pesanan = %s WHERE pesanan = %s"
            values = (nama, pesanan)
            self.mycursor.execute(query, values)
            self.mydb.commit()
            # Reset form dan tombol
            self.ids.nama_input.text = ""
            self.ids.pesanan_input.text = ""
            self.ids.tombol_simpan.text = "Tambah Data"
            self.ids.tombol_simpan.unbind(on_release=self.update_data_submit)
            self.ids.tombol_simpan.bind(on_release=self.show_data)
            # Refresh tabel
            self.show_table()
            self.show_success_popup("Data berhasil diperbarui!")
        except Exception as e:
            self.show_error_popup(f"Gagal memperbarui data: {e}")

    def show_error_popup(self, message):
        popup = Popup(title="Error", content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()

    def show_success_popup(self, message):
        popup = Popup(title="Sukses", content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()


    def delete_data(self, pesanan):
        try:        # Konfirmasi pop-up
            confirm_popup = Popup(
                title="Konfirmasi Hapus",
                content=Label(text=f"Yakin ingin menghapus data dengan pesanan =  {pesanan}?"),
                size_hint=(0.6, 0.4)
            )
            btn_layout = BoxLayout(spacing=10, size_hint_y=None, height=40)
            btn_yes = Button(text="Ya", size_hint_x=0.5)
            btn_no = Button(text="Batal", size_hint_x=0.5)

            # Tombol konfirmasi
            btn_yes.bind(on_press=lambda instance: self.confirm_delete(pesanan, confirm_popup))
            btn_no.bind(on_press=confirm_popup.dismiss)
            btn_layout.add_widget(btn_yes)
            btn_layout.add_widget(btn_no)
            
            confirm_popup.content = BoxLayout(orientation='vertical', spacing=10)
            confirm_popup.content.add_widget(Label(text=f"Yakin ingin menghapus data dengan PESANAN {pesanan}?"))
            confirm_popup.content.add_widget(btn_layout)
            confirm_popup.open()
        
        except Exception as e:
            self.show_error_popup(f"Gagal menghapus data: {str(e)}")
        
    def confirm_delete(self, pesanan , confirm_popup):
        try:
            # Hapus data dari database
            sql = "DELETE FROM tbl_pesanan WHERE pesanan = %s"
            val = (pesanan,)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            confirm_popup.dismiss()
            self.show_table()
        except Exception as e:
            self.show_error_popup(f"Gagal menghapus data: {str(e)}")

    def on_close(self):
        # Menutup koneksi database saat aplikasi ditutup
        self.mycursor.close()
        self.mydb.close()


class form(App):
    def build(self):
        self.root_widget = InputForm()
        return self.root_widget
        
    def on_start(self):
        self.root_widget.show_table()
        Window.size = (1000, 600)
        self.title = "Form Data KRIPIK21"
        self.icon = "logo.png"

    def on_stop(self):
        # Panggil metode untuk menutup koneksi database
        self.root_widget.on_close()

if __name__ == "__main__":
    form().run()
