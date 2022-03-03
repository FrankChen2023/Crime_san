import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
db_name = 'crime_data.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/date_search')
def date_search():
    return render_template('date_search.html')

@app.route('/position_search')
def position_search():
    return render_template('position_search.html')

@app.route('/date_result/<date>')
def date_result(date):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from crime_date WHERE date=?", (date,))
    rows = cur.fetchall()
    conn.close()
    return render_template('date_result.html', rows=rows)

@app.route('/position_result/<position>')
def position_result(position):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from crime_position WHERE district=?", (position,))
    rows = cur.fetchall()
    conn.close()
    return render_template('position_result.html', rows=rows)


@app.route('/total')
def total():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from crime_date")
    rows_date = cur.fetchall()
    cur.execute("select * from crime_position")
    rows_position = cur.fetchall()
    conn.close()
    return render_template('total.html', rows_date=rows_date, rows_position=rows_position)

@app.route('/coordinates_search', methods=["GET", "POST"])
def coordinates_search():
    longitude = '-'
    latitude = '3'
    if request.method=="POST":
        longitude = request.form["longitude"]
        latitude = request.form["latitude"]
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from crime_position WHERE longitude LIKE ? AND latitude LIKE ? ", (longitude+'%', latitude+'%'))
    rows = cur.fetchall()
    conn.close()
    return render_template("coordinates_search.html", rows=rows)


