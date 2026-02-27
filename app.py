import os
import uuid
import json
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
DATA_FILE = os.path.join(BASE_DIR, 'data.json')
ALLOWED_EXTENSIONS = {'mp4', 'webm', 'ogg', 'mov'}
MAX_CONTENT_LENGTH = 200 * 1024 * 1024  
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.secret_key = 'replace-this-with-a-secure-random-key'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def save_data(d):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect(url_for('upload'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'video' not in request.files:
            flash('Video dosyası seçilmedi.')
            return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            flash('Dosya ismi boş.')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            unique_name = f"{uuid.uuid4().hex}_{filename}"
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
            file.save(save_path)

           
            data = load_data()
            data[unique_name] = filename
            save_data(data)

           
            watch_url = url_for('watch', filename=unique_name, _external=True)
            return render_template('upload.html', success=True, watch_url=watch_url)

        else:
            flash('Geçersiz dosya formatı.')
            return redirect(request.url)

    return render_template('upload.html', success=False)

@app.route('/watch/<filename>')
def watch(filename):
    data = load_data()
    if filename not in data:
        flash('Video bulunamadı.')
        return redirect(url_for('upload'))

    
    repeats = 0
    if 'repeats' in request.args:
        try:
            repeats = int(request.args.get('repeats', 0))
        except ValueError:
            repeats = 0
    if 'loop' in request.args:
        repeats = 0  

    video_url = url_for('uploaded_file', filename=filename)
    return render_template('watch.html', video_url=video_url, repeats=repeats)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)