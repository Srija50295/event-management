from flask import Flask, render_template, request
from flask_mail import Mail, Message

import os
app = Flask(__name__)

# configuration of mail 
app.config['MAIL_DEBUG'] = True
app.config['MAIL_TIMEOUT'] = 60
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 465  # Typical port for SSL
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'srijanaluvalasrijanaluvala@gmail.com'
app.config['MAIL_PASSWORD'] = 'Srija@50295'
app.config['MAIL_DEFAULT_SENDER'] = 'kanugantipoojitha@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('first.html')

if __name__ == '__main__':
    app.run(debug=True)