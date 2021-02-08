import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    books = mongo.db.books.find()
    return render_template("books.html", books=books)


# Search books
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)


# Single Book Info
@app.route("/book/<book_id>")
def book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book.html", book=book)


# collect category
@app.route("/show_category")
def show_category():
    books = mongo.db.books.find()
    return render_template("show_category.html", books=books)


# User info
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # if form is posting checking db to find users
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if user is already registered
            flash("Sorry, this username is taken, try another!")
            return redirect(url_for("register"))

        register = {
            # if username not taken, sends form to database to store new user
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have been succesfully registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")): 
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome {}".format(request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))

            else:
                flash("Sorry, username and/or password is incorrect")
                return redirect(url_for('login'))

        else:
            flash("Sorry, username and/or password is incorrect")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    books = mongo.db.books.find()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    return render_template("profile.html", username=username, books=books)


@app.route("/logout")
def logout():
    flash("You have now been logged out! See you next time!")
    session.pop("user")
    return redirect(url_for("books"))


# Manage Books
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_category": request.form.get("book_category"),
            "book_description": request.form.get("book_description"),
            "book_image_url": request.form.get("book_image_url"),
            "created_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Book is now added to your collection!")
        return redirect(url_for("books"))

    categories = mongo.db.categories.find().sort("book_category", 1)
    return render_template("add_book.html", categories=categories)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_category": request.form.get("book_category"),
            "book_description": request.form.get("book_description"),
            "book_image_url": request.form.get("book_image_url"),
            "created_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Updated!")
        return redirect(url_for("books"))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("book_category", 1)
    return render_template("edit_book.html", book=book, categories=categories)


@app.route("/like_book/<book_id>", methods=["GET", "POST"])
def like_book(book_id):
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)}, {"$inc": {"likes": 1}})
    return redirect(url_for("books"))


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book is now deleted")
    return redirect(url_for("books"))


# Manage Categories
@app.route("/categories")
def categories():
    categories = list(mongo.db.categories.find().sort("book_category", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "book_category": request.form.get("book_category")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "book_category": request.form.get("book_category")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Updated")
        return redirect(url_for("categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted")
    return redirect(url_for("categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
