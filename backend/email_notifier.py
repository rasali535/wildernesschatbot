
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotifier:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        
    def send_lead_notification(self, name, email, phone):
        """Sends an email notification about a new lead."""
        sender_email = os.environ.get('EMAIL_USER')
        sender_password = os.environ.get('EMAIL_PASS')
        receiver_email = os.environ.get('EMAIL_RECEIVER', sender_email) # Default to self
        
        if not sender_email or not sender_password:
            print("Email Config Missing: EMAIL_USER or EMAIL_PASS not set.")
            return False
            
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = f"🦁 New Safari Lead: {name}"
            
            body = f"""
            New Lead Captured via Tumi Chatbot!
            
            Name: {name}
            Email: {email}
            Phone: {phone}
            
            Time: {os.environ.get('RENDER_ deploy_time', 'Just now')}
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            
            print(f"Email notification sent for lead: {name}")
            return True
            
        except Exception as e:
            print(f"Failed to send email notification: {e}")
            return False
