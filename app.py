import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    request_text = request.form['request']

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(request_text)
        if request_text.strip().lower().startswith('select'):
            results = cur.fetchall()
            return render_template('results.html', results=results)
        else:
            conn.commit()
            cur.execute('SELECT * FROM db')
            results = cur.fetchall()
            return render_template('results.html', results=results)
    except sqlite3.OperationalError as e:
        return 'Ошибка в запросе: {}'.format(str(e))
    except Exception as e:
        return 'Ошибка сервера: {}'.format(str(e))


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    app.run()
