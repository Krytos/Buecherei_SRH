from flask import Flask, render_template, request, url_for, redirect, session
from flask_paginate import Pagination, get_page_args, get_page_parameter
import execute

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    auswahl = request.form.get("auswahl")
    if auswahl is None:
        return render_template('index.html')
    elif auswahl.lower() == "add":
        return redirect(url_for('add'))
    elif auswahl.lower() == "delete":
        return render_template('delete.html')
    elif auswahl.lower() == "edit":
        return render_template('edit.html')
    elif auswahl.lower() == "search":
        return redirect(url_for('search'))

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
    id = request.form.get("id")
    if action == "Delete":
        execute.del_user(id)
    # if action == "Edit":
        # execute.update_user(id)

    total = execute.get_all_users().all()
    page = int(request.args.get('page', 1))
    per_page = 25
    offset = (page - 1) * per_page
    users = execute.get_all_users().limit(per_page).offset(offset)
    pagination = Pagination(page=page, total=len(total), record_name='users', per_page=per_page, bs_version=4, offset=offset)
    return render_template("nutzer.html", users=users, pagination=pagination)

@app.route('/buch', methods=["GET", "POST"])
def buch():
    return render_template("buch.html")

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