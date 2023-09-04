from secret import login, passwd, email_from, email_to
import smtplib, ssl



smtp_server = 'smtp.yandex.ru'
port = 465

letter = """From: mymail@gmail.com
To: friend@gmail.com
Subject: Привет!
Content-Type: text/plain; charset="UTF-8";

Привет!"""

letter = letter.encode("UTF-8")


server = smtplib.SMTP_SSL(smtp_server, port=port)

server.login(login, passwd)
server.sendmail(email_from, email_to, letter) # auth fails because security settings 
server.quit()