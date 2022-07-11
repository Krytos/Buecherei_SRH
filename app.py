from flask import Flask, render_template, request, url_for, redirect, session
import execute

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    test = request.form.get("auswahl")
    if test is None:
        return render_template('index.html')
    elif test.lower() == "add":
        return render_template('add.html')
    elif test.lower() == "delete":
        return render_template('delete.html')
    elif test.lower() == "edit":
        return render_template('edit.html')
    elif test.lower() == "search":
        return redirect(url_for('search'))

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        return render_template('add.html')
    else:
        return render_template('add.html')

# @app.route('/delete', methods=["GET", "POST"])
#
# @app.route('/edit', methods=["GET", "POST"])

@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search = request.form.get("search")
        users = execute.search_user(search)
        return render_template('list.html', users=users)
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run()
