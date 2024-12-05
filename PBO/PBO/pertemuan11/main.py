from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class HelloWorld(BoxLayout):
   pass
class HelloWorldApp(App):
   def build(self):
      return HelloWorld()
#metode build adalah metode khusus dalam app yang dipanggil saat aplikasi di jalankan

if __name__ == '__main__':
   HelloWorldApp().run()