import sys
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    print(request.json)
    return render_template("App.html")

if __name__ == '__main__':


    app.run()