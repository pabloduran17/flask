import datetime

from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route("/contact", methods=["POST"])
def contact():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        print(user_name)

        return render_template("about.html", name=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response


@app.route("/about-me")
def about_me():
    return render_template("about.html")

@app.route("/")
def index():
    return render_template("index.html")


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