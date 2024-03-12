from flask import Flask, request
from colorama import Fore

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask is working"


@app.route('/user', methods=['POST'])
def get_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        print(Fore.LIGHTBLUE_EX + "Username: ", Fore.LIGHTCYAN_EX + username, Fore.RESET + "\n",
              Fore.LIGHTBLUE_EX + "Password: ", Fore.LIGHTCYAN_EX + password + Fore.RESET, sep='')
        return '', 200
    elif not username or not password:
        return '', 401
    else:
        return '', 400


if __name__ == '__main__':
    # CONFIGURE SERVER IP
    app.run(host='192.168.100.99', port=5000, debug=True)
