from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/boogle")
def about_me():
    return render_template("boogle.html")

@app.route("/fakebook")
def portfolio():
    return render_template("fakebook.html")

@app.route("/hairsalon")
def portfolio_hairdress():
    return render_template("hair-salon.html")

@app.route("/portfolio")
def portfolio_facebook():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run()