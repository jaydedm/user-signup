from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route("/")
def index():

    return render_template('base.html')

if __name__ == "__main__":
    app.run()
