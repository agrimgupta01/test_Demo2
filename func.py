from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import datetime
app = Flask(__name__)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(secure_filename(f.filename))
        return 'file upload is success'
    if request.method == 'POST':
        y = request.date.get('date')
        y.save('date')
        return 'date saved'


if __name__ == '__main__':
    app.run(debug=True)
