import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.repositories.user_repository import UserRepository
from flask import flash 


app = Flask(__name__)
app.secret_key = os.urandom(24)

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
    session.clear() # Clears the entire session
    return redirect(url_for('get_index'))

@app.route('/')
@app.route('/index')
def get_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))