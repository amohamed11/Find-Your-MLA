import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    ridings = riding_list()

    return render_template('index.html', ridings=ridings, chosen='')


@app.route("/" , methods=['GET', 'POST'])
def show_minister():
    ridings = riding_list()
    if request.method == 'GET':
        chosen = ''
        return render_template('index.html', ridings=ridings, chosen=chosen)
    else:
        chosen = request.form['chose']
        print(chosen)
        return render_template('index.html', ridings=ridings, chosen=chosen)


    # c.execute('''SELECT * FROM ministers WHERE riding='%s' ''' % riding)
    # rows = c.fetchall
    # print(rows)

def riding_list():
    conn = sqlite3.connect("ministers.db")
    c = conn.cursor()

    c.execute('''SELECT riding FROM ministers ''')
    rows = c.fetchall()
    ridings = []
    for row in rows:
        ridings.append(row[0])
    ridings.sort()

    conn.close()

    return ridings

if __name__=='__main__':
    app.run()