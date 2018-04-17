from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True 
username= 'Jayde'

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        username = request.form['user-name']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        email = request.form['email']
        username_error = ''
        password_error = ''
        confirm_error = ''
        email_error = ''

        if username == '':
            username_error = "This is not a valid username"
        if ' ' in username:
            username_error = "This is not a valid username"
        if len(username) < 3 or len(username) >20:
            username_error = "This is not a valid username"
        if password == '':
            password_error = "This is not a valid password"
        if len(password) < 3 and len(password) >20:
            password_error = "This is not a valid password"
        if ' ' in password:
            password_error = "This password is invalid"
        if password != confirm_password:
            confirm_error = "Your passwords don't match"
        if email == "" or (len(email) >= 3 and len(email) <= 20) and ('.' in email and '@' in email) and " " not in email:
            email = email
        else:
            email_error = 'This email is invalid'
        
        rules = (username_error == "", password_error == "", confirm_error == "", email_error == '')
        
        if all(rules):
            return render_template('welcome.html', username=username)

        return render_template('form.html', username_error=username_error, 
        password_error=password_error, confirm_error=confirm_error,
        email_error=email_error, username=username, email=email)
        

@app.route('/welcome', methods = ['POST', 'GET'])
def logged_in():

    return render_template('welcome.html', username=username)

if __name__ == "__main__":
    app.run()


