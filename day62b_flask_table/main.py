from flask import Flask, render_template, Markup, request, url_for
from flask_table import Table, Col, LinkCol
import pandas as pd

app = Flask(__name__)

class SortableTable(Table):
    id = Col('ID')
    name = Col('Name')
    description = Col('Description')
    allow_sort = True
    description.allow_sort = False

    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction = 'desc'
        else:
            direction = 'asc'
        return url_for('index', sort=col_key, direction=direction)

@app.route('/')
def index():
    df = pd.read_csv("./day62_database_backend/example-table.csv", header=0, index_col=None)

    sort = request.args.get('sort', 'id')
    reverse = (request.args.get('direction', 'asc') == 'desc')

    df = df.sort_values(by=[sort], ascending=reverse)
    output_dict = df.to_dict(orient='records')

    table = SortableTable(output_dict,
                          sort_by=sort,
                          sort_reverse=reverse)
    return table.__html__()


# use header and data as separate import variables
# use BEM CSS to style the different parts of your table
# @app.route("/")
# def home():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
