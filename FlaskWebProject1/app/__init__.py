'''
Author: Daniel Herrera
Date: jan 30,2020
DESCRIPTION: 
    Flask server used to load my website and web services provided by my applications

'''

from flask import *
import numpy as np
app : Flask = Flask(__name__)


'''

'''
@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def pg_home() -> None:
    a : int = a
    return render_template("home_page.html")


'''
'''
@app.route("/resume", methods=['GET', 'POST'])
def pg_resume() -> None:
    if request.method == "POST":
        return redirect(url_for('pg_home'))
    return render_template("home_page.html") 


'''
'''
@app.route("/projects", methods=['GET', 'POST'])
def pg_projects():
    if request.method == "POST":
        return redirect(url_for('pg_home'))
    return render_template("home_page.html") 


'''
'''
@app.route("/contact", methods=['GET', 'POST'])
def pg_contact():
    if request.method == "POST":
        return redirect(url_for('pg_home'))
    return render_template("home_page.html") 


'''
'''
@app.route("/admin", methods=['GET', 'POST'])
def admin() -> None: return "admin"
    

if __name__ == "__main__":
    app.run(debug=True)