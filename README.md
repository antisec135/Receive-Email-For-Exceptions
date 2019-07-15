# Receive-Email-For-Exceptions
This python script sends an email every time an exception is generated using SMTP SSL

I created this script to help with python exceptions, I was struggling with how to manage my script logs. I've decided to create this script to send errors by email on every exception happened on the script.


Change the file with your SMTP credentials, I used the AWS SES service and it worked well with it. Alternatively, if you aren't using SSL you can use the pre-build class logging.handlers.SMTPHandler()

Import this file to your script after changing the credentials
