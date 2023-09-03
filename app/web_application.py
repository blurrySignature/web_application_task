from flask import Flask
import os
from dotenv import load_dotenv
import uuid

app = Flask(__name__)

# Если uuid не задан, то генерируем его и заносим в .env
with open('.env', 'r') as env_file:
    lines = env_file.readlines()
    uuid_exists = any(line.startswith('UUID=') for line in lines)
if not uuid_exists:
    with open('.env', 'a') as env_file:
        new_uuid = str(uuid.uuid4())
        env_file.write(f'UUID={new_uuid}\n')

load_dotenv()

hostname = os.getenv('COMPUTERNAME') if os.name == 'nt' else os.uname().nodename
author = os.getenv('AUTHOR')
user_id = os.getenv('UUID')


@app.route('/')
def index():
    return 'index page'


@app.route('/healthcheck')
def healthcheck_result():
    return 'OK! It is running...'


@app.route('/hostname')
def get_hostname():
    return hostname


@app.route('/author')
def get_author():
    return author


@app.route('/id')
def get_id():
    return user_id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
