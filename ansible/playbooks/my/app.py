import os
from dotenv import load_dotenv

from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import socket

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
app = Flask(__name__)


def test() -> str:
    return 'Куэйяр Егоров Андрей'

@app.route('/')
def index() -> str:
    return test()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
