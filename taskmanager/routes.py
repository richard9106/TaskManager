""" Importamos lo que necesitamos """
from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    """ renderizamos base html """
    tasks = list(Task.query.order_by(Task.task_name).all())
    return render_template("task.html", tasks=tasks)


@app.route("/categories")
def categories():
    """render template categories"""
    thecategories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=thecategories)


@app.route("/add_categories", methods=["GET", "POST"])
def add_categories():
    """render template categories"""
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_categories/<int:category_id>", methods=["GET", "POST"])
def edit_categories(category_id):
    """render template categories"""
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_categories/<int:category_id>", methods=["GET", "POST"])
def delete_categories(category_id):
    """render template categories"""
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))
   


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    """render template categories"""
    thecategories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id") 
        )

        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=thecategories)

@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    """render template categories"""
    task = Task.query.get_or_404(task_id)
    thecategories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_task.html", task=task, categories=thecategories)
