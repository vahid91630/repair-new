from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'ربات تعمیرکار آنلاین و فعاله 💥'
