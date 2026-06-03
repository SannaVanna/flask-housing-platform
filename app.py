import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# uploading files
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# connecting with sqlalchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class EmailEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        #     display post data
        name = request.form.get('name')
        email = request.form.get('email')
        address = request.form.get('address')
        message = request.form.get('message')

        new_entry = EmailEntry(name=name, email=email, address=address, message=message)
        db.session.add(new_entry)
        db.session.commit()
        return render_template('submit.html', name=name)
    return render_template("contact.html")


@app.route('/upload')
def upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # uploaded_file_url = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part in form'
        file = request.files['file']
        if file.filename == '':
            return 'No file selected'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        return render_template('upload-success.html', filename=filename)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2000, debug=True)
