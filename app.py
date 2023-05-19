import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        request_text = request.form['request']

        try:
            query = request_text.split(';')[0]  # Extract main query before ;

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(query)

            if query.strip().lower().startswith('select'):
                results = cur.fetchall()
                return render_template('index.html', results=results, error_message=None, request=request_text)

            conn.commit()
            cur.execute('SELECT * FROM db')
            results = cur.fetchall()
            return render_template('index.html', results=results, error_message=None, request=request_text)

        except sqlite3.Error as e:
            return render_template('index.html', results=None, error_message=str(e), request=request_text)

    return render_template('index.html', results=None, error_message=None, request='')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    app.run()
