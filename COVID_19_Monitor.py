from flask import Flask, render_template
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
# POST to API


app = Flask(__name__)
@app.route('/data_plot', methods=['POST', 'GET'])
def plot():
    payload = {'country': 'Italy'}
    URL = 'https://api.statworx.com/covid'
    response = requests.request("POST", url=URL, data=json.dumps(payload))

    df = pd.DataFrame.from_dict(json.loads(response.text))

    fig = plt.figure(figsize=(8, 6))
    plt.plot(df["cases_cum"], 'bo')
    fig.suptitle("Country: Italy")
    plt.xlabel("Number of days since 1/1/2020")
    plt.ylabel("Number of cases")
    img = plt.savefig('static/imgs/Italy.png')
    return render_template('result_plot.html', url = 'static/imgs/Italy.png')


@app.route('/data')
def data():
    payload = {'country': 'Italy'}
    URL = 'https://api.statworx.com/covid'
    response = requests.request("POST", url=URL, data=json.dumps(payload))

    df = pd.DataFrame.from_dict(json.loads(response.text))

    return render_template('result.html', data = {'Italy': df['cases_cum'].values} )

@app.route('/')
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.run()