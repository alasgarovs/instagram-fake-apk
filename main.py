from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.utils import rgba
import webbrowser

Window.size = (400, 680)


class InstagramApp(MDApp):
    def build(self):
        return Builder.load_file('insta-login.kv')

    def on_login(self, username, password):
        if username.strip() == "" or password.strip() == "":
            self.show_error_dialog("Error", "Username or password cannot be empty!")
        else:
            link = "https://instagram.com/"+str(username)
            webbrowser.open(link)
            # print(username, password)

    def show_error_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[MDRaisedButton(text="OK", on_release=self.dismiss_dialog)])

        dialog.ids.text.text_color = rgba("#000000")
        dialog.open()

    def dismiss_dialog(self, *args):
        for dialog in MDApp.get_running_app().root_window.children:
            if isinstance(dialog, MDDialog):
                dialog.dismiss()


if __name__ == '__main__':
    InstagramApp().run()
