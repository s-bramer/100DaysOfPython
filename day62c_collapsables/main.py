from flask import Flask, render_template, Markup, request, url_for
from flask_bootstrap import Bootstrap
from flask_table import Table, Col, LinkCol
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
Bootstrap(app)

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cafes')
def cafes():
    with open('./day62_database_backend/events_database_no_desc.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)
    
if __name__ == '__main__':
    app.run(debug=True)
