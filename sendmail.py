import smtplib

sender = "pimessage@yandex.com"
receiver = "pimessage@protonmail.com"
password = "NicoNicoPy66"
subject = "Python email test"
body = "ALERT ALERT ALERT"

# header
message = f"""From: Rasputin Pi{sender}
To: Michael Burry{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.yandex.com", 465)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
