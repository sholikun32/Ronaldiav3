from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"

# Wajib: Buat variabel `app` yang bisa diimport
if __name__ == '__main__':
    app.run()
