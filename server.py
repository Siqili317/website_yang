from flask import Flask, render_template, request
import datetime, smtplib, os

app = Flask(__name__)
my_email = os.environ.get("WEB_GMAIL")
my_password = os.environ.get("WEB_GMAIL_PASSWORD")
# def copyright(function):
#     def wrapper(*args, **kwargs):
#         today = datetime.date.today()
#         year = today.strftime("%Y")
#         function(year)
#     return function


@app.route("/")
def get_home():
    today = datetime.date.today()
    year = today.strftime("%Y")
    return render_template('index.html', current_year = year)

@app.route("/project")
def get_project():
    today = datetime.date.today()
    year = today.strftime("%Y")
    return render_template('project.html', current_year = year)

@app.route("/teaching")
def get_teaching():
    today = datetime.date.today()
    year = today.strftime("%Y")
    return render_template('teaching.html', current_year = year)

@app.route("/publications")
def get_publication():
    today = datetime.date.today()
    year = today.strftime("%Y")
    return render_template('publication.html', current_year = year)

@app.route("/contact", methods = ["GET", "POST"])
def get_contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["subject"], data["message"])
        return f"<h1>Successfully sent your message!</h1><p>Thank you, {request.form['name']}! I will get back to you soon. --Yang"
    return render_template('contact.html')

def send_email(name, email, subject, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {subject}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", "587") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr= my_email, to_addrs= "yangy48@gmail.com", msg = email_message)

if __name__ == "__main__":
    app.run(debug=True)