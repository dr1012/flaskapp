from flask import render_template, Flask, flash, redirect, request, url_for, send_from_directory
from config import Config
from forms import LoginForm, UploadFileForm
from werkzeug.utils import secure_filename
import os
from pdf_extractor import extract
from frequency_distribution import frequency_dist
from mywordcloud import build_word_cloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import urllib.parse

app = Flask(__name__)

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'zip', 'tar', 'rar', '7z', 'tgz'])




app.config.from_object(Config)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024


@app.route('/')
def hello():
    uploadForm = UploadFileForm()
    return render_template('home.html',title = 'Welcome', form = uploadForm)




'''
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print('WOOP WOOP')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'document' not in request.files:
            print("file not in request.files")
            flash('No file part')
            return redirect(request.url)
        file = request.files['document']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))
            x, y, word_list = extract(os.path.join('uploads', filename))
            graph_data = frequency_dist(word_list, 50, ('Word frequency for file  with filename: ' + filename))
            build_word_cloud(word_list, 2000)
            return render_template('analysis_options.html', title='NLP analysis',filename = filename, graph_data = graph_data)
            
   
        else:
            flash('not an allowed file format')
            return redirect(url_for('upload_file'))

'''


'''
@app.route('/pygalexample/')
def pygalexample():
    test = ['hello', 'world', 'hello', 'my', 'name', 'is', 'david']
    graph_data = frequency_dist(test, 5)
    return dict(graph_data=graph_data)


app.jinja_env.globals.update(clever_function=pygalexample)
'''



if __name__ == '__main__':
  app.run()