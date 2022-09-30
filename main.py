from datetime import date

from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html',date = date.today(),all_news = 1,persons_today = 2)


if __name__ == "__main__":
    app.run()