import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import time

UPLOAD_FOLDER = './download'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    print("hello")
    return "hello"

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        start_ticks = time.time()
        print("start upload", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_ticks)))
        file = request.files['file']
        filename = file.filename
        size = len(file.read())
    
        print(str(size))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finish_ticks = time.time()
        print("finish upload", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(finish_ticks)))
        use_time = finish_ticks - start_ticks
        speed = round(size / 1024 / 1024 / use_time, 2) 
        print("upload  " + filename + " : " + str(speed) + "MB/s")
        return '{"status":success}'
    return 'need post'


if __name__ == "__main__":
    app.run(
        debug = True,
        port = 8088
    )