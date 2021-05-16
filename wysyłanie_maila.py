import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
print(conn.ehlo())
conn.starttls()

conn.login('login@gmail.com', 'password')

conn.sendmail('from@gmail.com', 'to@gmail.com', 'Subject: Temat\n\nTreść maila\n\n-Podpis')

conn.quit() # zamknięcie połączenia
