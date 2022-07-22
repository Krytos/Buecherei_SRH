from flask import Flask, render_template, request, url_for, redirect, session
from flask_paginate import Pagination
import execute

app = Flask(__name__)

def paginate(query, per_page=25):
    total = query.count()
    page = int(request.args.get('page', 1))
    items = query.offset((page -1)* per_page).limit(per_page).all()
    pagination = Pagination(page=page, total=total, record_name='items', per_page=per_page, css_framework="bootstrap5")
    return items, pagination

@app.route('/', methods=["GET", "POST"])
def index():
    auswahl = request.form.get("auswahl")
    if auswahl is None:
        return render_template('index.html')

@app.route('/popup', methods=["GET", "POST"])
def popup():
    return render_template('popup.html')

@app.route('/add', methods=["GET", "POST"])
def add():
    auswahl = request.form.get("auswahl")
    if auswahl is None:
        return render_template("add.html")
    else:
        return render_template("add.html", auswahl=auswahl)

@app.route('/nutzer', methods=["GET", "POST"])
def nutzer():
    action = request.form.get("action")
    edit = request.form.getlist("edit")
    id = request.form.get("id")
    if action == "Delete":
        execute.del_user(id)
    if edit:
        execute.update_user(edit[0], edit[1], edit[2], edit[3], edit[4])
    users, pagination = paginate(execute.get_all_users())
    return render_template("nutzer.html", users=users, pagination=pagination)

@app.route('/buch', methods=["GET", "POST"])
def buch():
    action = request.form.get("action")
    edit = request.form.getlist("edit")
    id = request.form.get("id")
    if action == "Delete":
        execute.del_buch(id)
    if edit:
        execute.update_buch(edit[0], edit[1], edit[2], edit[3])
    books, pagination = paginate(execute.get_all_books())
    return render_template("buch.html", books=books, pagination=pagination)

@app.route('/ausleih', methods=["GET", "POST"])
def ausleih():
    return render_template("ausleih.html")

@app.route('/search', methods=["GET", "POST"])
def search():
    auswahl = request.form.get("auswahl")
    search = request.form.get("search")

    if str(auswahl).lower() == "nutzer.html":
        if search:
            return render_template("search.html", auswahl=auswahl.lower(), users=execute.search_user(search))
        return render_template("search.html", auswahl=auswahl.lower())
    elif str(auswahl).lower() == "buch":
        if search:
            return render_template("search.html", auswahl=auswahl.lower(), books=execute.search_book(search))
        return render_template("search.html", auswahl=auswahl.lower())
    else:
        return render_template("search.html")


if __name__ == '__main__':
    app.run()