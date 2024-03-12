# Instagram login app for android devices

This simple application written by Kivy framework of Python language and KivyMD for logging into instagram.
This is a fake instagram login app.

![instagram](https://github.com/alasgarovs/instagram-fake-apk/assets/70092601/4bcdf3cc-391e-430a-b3b3-9cd1cb343643)


## Features

- Allows users to enter their username and password.
- Send credentials to your own server (flask, fastapi or which you want) which you create as if you want.
- Validates the input and displays an error message and etc.

## Installation and Usage

1. Clone the repository.
```bash
git clone https://github.com/alasgarovs/instagram-fake-apk.git
```

2. Install the required dependencies.
```bash
pip install -r requirements.txt
```

3. Configure the IP address of the server in server.py and run it so the server will listen to capture your username and password from your application.
```bash
python server.py
```

4. Set ```flask_server_ip_last_octet``` in main.py to be the same as the last octet of the server IP and run main.py.
```bash
python main.py
```

## Disclaimer

This program is made for learning and testing purposes only. The developer is not responsible for any situations that may occur while using this application.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

