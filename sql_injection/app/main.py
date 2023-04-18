from flask import Flask, render_template, url_for, request, redirect, g
import sqlite3, os

app = Flask(__name__)
app.database = "main.db"
res = []


def connect_db():
    return sqlite3.connect(app.database)


@app.route('/', methods=['GET', 'POST'])
def index():
    global res
    res = []
    if request.method == 'POST':
        id = request.form['id']
        g.db = connect_db()
        curs = g.db.execute("SELECT * FROM Student WHERE id = '%s'" % id)
        results = [dict(id=row[0], name=row[1], scholarship=row[2], passport=row[3], email=row[4]) for row in curs.fetchall()]
        g.db.close()
        for k in results:
            for i in k:
                a = i + ": " + str(k[i])
                res.append(a)
            res.append("")
        return redirect('/check')
    else:
        return render_template('index.html')


@app.route('/check')
def check():
    global res
    if len(res) == 0:
        res.append("Invalid User ID")
    return render_template("check.html", lip=res)


@app.route('/about')
def about():
    global res
    res = []
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('error.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error=error)


if __name__ == "__main__":
    if not os.path.exists(app.database):
        with sqlite3.connect(app.database) as connection:
            c = connection.cursor()
            c.execute("""CREATE TABLE Student(id TEXT, name TEXT, scholarship TEXT, passport TEXT, email TEXT)""")
            c.execute("""CREATE TABLE medical_notes(id TEXT, value TEXT)""")
            c.execute("""CREATE TABLE privileges(id TEXT, value TEXT)""")
            c.execute('INSERT INTO Student VALUES("4568634", "Clash Royale", "1", "9001 000101", "c.royale2007@ui.ru")')
            c.execute('INSERT INTO Student VALUES("1", "Hafeez Baraf", "18000", "9001 176532", "h.baraf1977@ui.ru")')
            c.execute('INSERT INTO Student VALUES("6661337", "X", "99999", "6666 666228", "superuser@ui.ru")')
            c.execute('INSERT INTO Student VALUES("91929394","Ichigo Kurosaki", "1424", "9001 000001", "i.k@ui.ru")')
            c.execute('INSERT INTO medical_notes VALUES("4568634", "98eb470b2b60482e259d28648895d9e1")')
            c.execute('INSERT INTO medical_notes VALUES("1", "b489ffabf08511b2738f966b52bed418")')
            c.execute('INSERT INTO medical_notes VALUES("6661337", "6651b15eeb730854d66b654f00778425")')
            c.execute('INSERT INTO medical_notes VALUES("91929394", "387e6278d8e06083d813358762e0ac63")')
            c.execute('INSERT INTO privileges VALUES("4568634", "user")')
            c.execute('INSERT INTO privileges VALUES("1", "user")')
            c.execute('INSERT INTO privileges VALUES("6661337", "admin")')
            c.execute('INSERT INTO privileges VALUES("91929394", "user")')
            connection.commit()
            connection.close()
    app.run(host='0.0.0.0', debug=False)
