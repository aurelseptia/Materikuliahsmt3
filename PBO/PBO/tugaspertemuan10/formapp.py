from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

class InputForm(BoxLayout):
    def show_data(self):
        # Ambil data dari text input
        nama = self.ids.nama_input.text
        nim = self.ids.nim_input.text
        jurusan = self.ids.jurusan_input.text

        # Format data untuk ditampilkan
        data = f"Nama: {nama}\nNIM: {nim}\nJurusan: {jurusan}"

        # Buat popup
        popup_content = BoxLayout(orientation="vertical")
        popup_content.add_widget(Label(text=data))

        close_btn = Button(text="Tutup", size_hint_y=None, height=40)
        close_btn.bind(on_release=lambda x: popup.dismiss())

        popup_content.add_widget(close_btn)

        popup = Popup(
            title="Data Mahasiswa",
            content=popup_content,
            size_hint=(0.8, 0.4),
            auto_dismiss=False,
        )
        popup.open()


class FormApp(App):
    def build(self):
        # Load layout dari file .kv
        return InputForm()


if __name__ == "__main__":
    FormApp().run()