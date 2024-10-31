from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from flask_login import login_required, login_user, current_user, logout_user
from flask_session import Session
from fashion import create_app
from .models import create_user, get_user, User
from .login_manager_setup import login_manager


app = create_app('development')


login_manager.init_app(app)
bcrypt = Bcrypt(app)

app.config['DEBUG'] = True

app.config['SECRET_KEY'] = 'secret'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json(force=True)
        full_name = data['Full name']
        email = data['Email']
        password = data['Password']
        phone = data['Phone number']

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

          # Create a new user document
        userdata = {
            "fullname": full_name,
            "email": email,
            "password_hash": password_hash, # You should hash the password before storing it
            "phone_number": phone
        }
        new_user = create_user(userdata) 
        # print the return value of user_id

         # Redirect to a success page or show a success message
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json(force=True)
        # Safely retrieve email and password from the data
        email = data.get('email')
        password = data.get('password')

        # Check if the required fields are present
        if not email or not password:
            return jsonify({'status': 'error', 'message': 'Missing email or password'}), 400
        
        user = User.objects(email=email).first()

        if user is None:
            return jsonify({
                'message': 'User not found.',
                'status': 'error',
                'email': email,
                'password': password  # Be cautious with password exposure
            }), 401
        
        if bcrypt.check_password_hash(user.password_hash, password):
            login_user(user, force=True)
            session['logged_in'] = True
            session['username'] = user.fullname
            session['user_email'] = email
            return jsonify({  # Fix: properly indent this line
                'message': 'Login successful!',
                'status': 'success',
                'redirect': url_for('dashboard')
            })
        else:
            return jsonify({'message': 'Invalid username or password.', 'status': 'error'})
            
    return render_template('login.html')



@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
    if current_user.is_authenticated:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/blog/create', methods=['POST'])
@login_required
def create_blog():
    title = request.form.get('title')
    content = request.form.get('content')
    post = BlogPost(title=title, content=content, author=current_user._get_current_object())
    post.save()
    flash("Blog post created successfully!")
    return redirect(url_for('view_blog', post_id=post.id)) 

@app.route('/indexx')
@login_required
def indexx():
    if current_user.is_authenticated:
        return render_template('indexx.html')
    else:
        return redirect(url_for('login'))

@app.route('/about')
@login_required
def about():
    if current_user.is_authenticated:
        return render_template('about.html')
    else:
        return redirect(url_for('login'))

@app.route('/guides')
@login_required
def guides():
    if current_user.is_authenticated:
        return render_template('guides.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('logged_in'):
        session.pop('logged_in', None)
        session.pop('username', None)
        session.pop('user_email', None)
        logout_user()  # If using Flask-Login
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)
