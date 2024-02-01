""" Importamos lo que necesitamos """
from flask import render_template, request, redirect, url_for
from taskmanager import app, db 
from taskmanager.models import Category, Task 


@app.route("/")
def home():
    """ renderizamos base html """
    return render_template("task.html")


@app.route("/categories")
def categories():
    """render template categories"""
    return render_template("categories.html")


@app.route("/add_categories", methods=["GET", "POST"])
def add_categories():
    """render template categories"""
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
