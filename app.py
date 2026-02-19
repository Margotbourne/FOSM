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
        
        if email == "admin@example.com" and password == "secret":
            session['user_id'] = 1 
            flash("Welcome back!") # This message shows up on the next page
            return redirect(url_for('account')) 
        else:
            flash("Invalid email or password.") # Sends feedback
            return redirect(url_for('login')) # Keeps them on the login page

    return render_template('login.html')

@app.route('/account') 
def account():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # You can pass user data here later
    return render_template('account.html')

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