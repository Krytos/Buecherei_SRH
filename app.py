from flask import Flask, render_template, request, url_for, redirect, session
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

# @app.route('/delete', methods=["GET", "POST"])
#
# @app.route('/edit', methods=["GET", "POST"])

@app.route('/search', methods=["GET", "POST"])
def search():
    auswahl = request.form.get("auswahl")
    search = request.form.get("search")

    if str(auswahl).lower() == "nutzer":
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