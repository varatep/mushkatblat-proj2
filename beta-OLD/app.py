import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_url_path="")
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route("/")
def root():
    return app.send_static_file("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["GET", "POST"])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        # return redirect(url_for('uploaded_file',
                                # filename=filename))
    # file = request.files['file']
    # extension = os.path.splitext(file.filename)[1]
    # f_name = str(uuid.uuid4()) + extension
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
    # return json.dumps({'filename': f_name})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, debug=True)
