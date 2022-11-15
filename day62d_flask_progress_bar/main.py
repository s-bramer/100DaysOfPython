import scraper
import requests
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for
from threading import Thread
from time import sleep
import json


app = Flask(__name__)
status = None
event_pages_data = "./day62d_flask_progress_bar/event_pages.csv"

def task():
    global status
    df_in = pd.read_csv(event_pages_data, header=0, index_col=None)
    df_out_path = "./day62d_flask_progress_bar/events_database.csv"
    df_out = pd.DataFrame()
    for i, row in enumerate(range(0, len(df_in))):
        link = str(df_in.iloc[row]['link'])
        df_out = pd.concat(objs=[df_out, scraper.run_scraper(link, row, df_in)])
        print(f"EVENTS: {len(df_out)}")
        status = (i+1)*(10/len(df_in))
    #SAVE DATAFRAME AS CSV
    #first sort by sort_date
    df_out = df_out.sort_values(by='sort_date',ascending=True,ignore_index=True)
    #then remove month duplicates (for month subsection labels)
    current_month = ""
    for row in range(0, len(df_out)):
        if df_out.loc[row, ('month')] != current_month:
            current_month = df_out.loc[row, ('month')]
        else:
            #print(f"{df_out.loc[row, ('title')]} month {df_out.loc[row, ('month')]} deleted from row {row}")
            df_out.loc[row, ('month')] = ""
    df_out.to_csv(df_out_path,index=False)


@app.route('/', methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        print(request.form.get)
        if request.form.get('test') != None:
            print("LETS RELOAD!!!!!!!!!")
            t1 = Thread(target=task)
            t1.start()
            # return redirect(url_for('index'))
        else:
            print(request.form.get('test'))
    return render_template('index.html')
  
@app.route('/status', methods=['GET'])
def getStatus():
    print("status retrieved...")
    statusList = {'status':status}
    return json.dumps(statusList)

if __name__ == '__main__':
    app.run(debug=True)