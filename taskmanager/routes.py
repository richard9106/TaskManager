""" Importamos lo que necesitamos """
from flask import render_template
from taskmanager import app, db 
from taskmanager.models import Category, Task 


@app.route("/")
def home():
    """ renderizamos base html """
    return render_template("task.html")
