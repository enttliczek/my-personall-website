from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
OWN_PASSWORD = "ticlwpdamrxwrpul"

app = Flask(__name__)


def send_mail(name, email, message):

    #Create a email configuration
    sender_mail = "daddygocode@gmail.com"
    receiver_mail = "bentkowski.kamil@gmail.com"
    subject = "New contact from MyWebsite"

    #Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_mail
    msg['To'] = receiver_mail
    msg['Subject'] = subject

    #Attached the message body
    body = f'Name: {name}\nEmail: {email}\nMessage: {message} '
    msg.attach(MIMEText(body, 'plain'))

    #Connect to the SMTP server and send the mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(sender_mail, OWN_PASSWORD)
        connection.sendmail(sender_mail, receiver_mail, msg.as_string())


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        send_mail(name, email, message)
        return redirect(url_for('home'))

    return render_template('error.html', error='Method Not Allowed'), 405









if __name__ == ("__main__"):
    app.run(debug=True)

