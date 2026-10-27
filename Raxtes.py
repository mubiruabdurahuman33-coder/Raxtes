import threading
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>RAXTES READY</h1><p>Build success!</p>"

def run_flask():
    app.run(port=5000, debug=False)

if __name__ == '__main__':
    t = threading.Thread(target=run_flask, daemon=True)
    t.start()
    time.sleep(1)
    try:
        import webview
        webview.create_window("RAXTES", "http://127.0.0.1:5000", width=1000, height=700)
        webview.start()
    except:
        print("RAXTES at http://127.0.0.1:5000")
        while True:
            time.sleep(1)
