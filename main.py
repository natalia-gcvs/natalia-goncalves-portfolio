from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from forms import ContactForm
import secrets
import smtplib
import os


def send_email(name, email, subject, message):
    smtp_username = os.environ['smtp_email']
    smtp_password = os.environ['smtp_email_password']
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=smtp_username, password=smtp_password)
        connection.sendmail(from_addr=smtp_username, to_addrs=os.environ['from_to_address'],
                            msg=f'Subject: {subject}\n\n{name}\n{email}\n{message}')

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

# Cross-Site Request Forgery Protection
csrf = CSRFProtect(app)

# Bootstrap
bootstrap = Bootstrap(app)


from flask import jsonify

@app.route("/", methods=['GET', 'POST'])
def home():
    contact_form = ContactForm()
    print(contact_form.data)
    if contact_form.validate_on_submit():
        print("message delivered")
        data = contact_form.data
        send_email(data['name'], data['email'], data['subject'], data['message'])
        return render_template('index.html', form=contact_form)
    return render_template('index.html', form=contact_form)




if __name__ == '__main__':
    app.run(debug=True)