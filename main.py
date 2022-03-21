from flask import Flask, render_template, request
# import requests
import smtplib

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":

        email = request.form["EMAIL"]
        mail_msg = f" {email} subscribed for your newsletter."
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="ajaxmemo@gmail.com", password="")
            connection.sendmail(
                from_addr="ajaxmemo@gmail.com",
                to_addrs="ajaxmemo@gmail.com",
                msg=f"Subject: Portfolio newsletter Message\n\n{mail_msg}."
            )

    return render_template("index.html")

@app.route('/about')
def about():

    return render_template("about.html")


@app.route('/services')
def services():

    return render_template("services.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        mail_msg = f"Name : {name}\n Email : {email}\n subject : {subject}\n Message : {message}."
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="ajaxmemo@gmail.com", password="")
            connection.sendmail(
                from_addr="ajaxmemo@gmail.com",
                to_addrs="ajaxmemo@gmail.com",
                msg=f"Subject: Portfolio Contact Message\n\n{mail_msg}."
            )


    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)