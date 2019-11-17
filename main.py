import datetime

from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")

@app.route("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)


@app.route("/boogle", methods=["GET"])
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