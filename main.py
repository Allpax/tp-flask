import os
import sys

from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Menu():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)

