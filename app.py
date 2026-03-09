import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.repositories.user_repository import UserRepository
from flask import flash 
from flask import request, redirect, url_for
from datetime import date
from lib.models.gallery import GalleryPhoto
from lib.repositories.gallery_repository import GalleryRepository
from werkzeug.utils import secure_filename  # <--- Add this line
from lib.repositories.news_repository import NewsRepository
from lib.models.news import News
from werkzeug.utils import secure_filename 
from datetime import datetime


app = Flask(__name__)
app.secret_key = os.urandom(24)



UPLOAD_FOLDER = 'static/gallery_uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# --- THE MAGIC BIT ---
# This makes 'logged_in' available in every HTML template automatically
@app.context_processor
def inject_user_status():
    return dict(logged_in=('user_id' in session))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        user = repository.find_by_email(email)

        if user is not None and user.password_hash == password:
            session['user_id'] = user.id  
            return redirect(url_for('account')) 
        else:
            flash("Invalid email or password.") 
            return redirect(url_for('login')) 

    return render_template('login.html')


@app.route('/account')
def account():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    current_user = repository.find(session['user_id']) 
    return render_template('account.html', user=current_user)
   
@app.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('get_index'))


@app.route('/need')
def the_need():
    return render_template('need.html') 



@app.route('/gallery', methods=['GET'])
def get_gallery():
    connection = get_flask_database_connection(app)
    repository = GalleryRepository(connection)
    photos = repository.all()
    return render_template('gallery.html', photos=photos)

@app.route('/back_gallery', methods=['GET'])
def back_gallery():
    connection = get_flask_database_connection(app)
    repository = GalleryRepository(connection)
    photos = repository.all()
    return render_template('back_gallery.html', photos=photos)

@app.route('/upload-photo', methods=['POST'])
def upload_photo():
    connection = get_flask_database_connection(app)
    repository = GalleryRepository(connection)

    title = request.form.get('title')
    caption = request.form.get('caption')
    file = request.files.get('photo')

    if file and file.filename != '':
        # 1. Secure the filename and save the physical file
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # 2. Save the metadata to the database
        new_photo = GalleryPhoto(None, title, caption, filename)
        repository.add(new_photo)
        
        flash("Photo uploaded successfully!")
        return redirect(url_for('back_gallery'))
    
    flash("No file selected.")
    return redirect(request.referrer)


@app.route('/gallery/delete/<int:id>', methods=['POST'])
def delete_photo(id):
    connection = get_flask_database_connection(app)
    repository = GalleryRepository(connection)
    repository.delete(id)
    
    flash("Photo deleted.")
    return redirect(url_for('back_gallery'))


@app.route('/news')
def get_news():
    connection = get_flask_database_connection(app)
    repository = NewsRepository(connection)
    newses = repository.all() # Matches 'newses' in your HTML loop
    return render_template('news.html', newses=newses)

from werkzeug.utils import secure_filename

# --- ADD THIS AT THE TOP ---
# These are the only formats browsers can "view" directly
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# ---------------------------

@app.route('/upload_news', methods=['POST'])
def upload_news():
    connection = get_flask_database_connection(app)
    repository = NewsRepository(connection)

    title = request.form.get('title')
    content = request.form.get('content') or "Article Document"
    file = request.files.get('news_image')

    # CHECK: Does the file exist and is it a PDF/Image?
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        upload_folder = os.path.join(base_path, 'static', 'news_uploads')
        
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        
        new_item = News(None, title, content, datetime.now(), filename)
        repository.create(new_item)
        return redirect(url_for('back_news'))
    
    else:
        # This runs if the file is a .docx or other non-viewable format
        return "Invalid file type. Please upload a PDF or an Image so users can view it.", 400
    
# 3. THE BACK PAGE (Matches the URL you typed in browser)
@app.route('/back_news')
def back_news():
    connection = get_flask_database_connection(app)
    repository = NewsRepository(connection)
    all_articles = repository.all()
    # We change 'newses' to 'articles' to match your HTML loop
    return render_template('back_news.html', articles=all_articles)

# 5. DELETE ROUTE
@app.route('/delete_news/<int:id>', methods=['POST'])
def delete_news(id):
    connection = get_flask_database_connection(app)
    repository = NewsRepository(connection)
    # repository.delete takes news_id, so we pass 'id'
    repository.delete(id)
    return redirect(url_for('back_news'))


@app.route('/')
@app.route('/index')
def get_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))