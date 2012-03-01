
import csv
import smtplib
from email.mime.text import MIMEText


EMAIL_SENDER = 'rxin@cs.berkeley.edu'
SMTP_SERVER = ''
SMTP_USERNAME = ''
SMTP_PASSWORD = ''


gradesReader = csv.reader(open('grades.csv', 'rb'))
headerRow = gradesReader.next()

for row in gradesReader:
    if len(row) > 2:
        name = row[0]
        email = row[1]
        
        body = ''
        for (header, value) in zip(headerRow, row):
            body += '%s: %s\n' % (header, value)
        
        print 'emailing %s <%s>' % (name, email)

        msg = MIMEText(body)
        msg['Subject'] = 'CS194-16 Data Science Assignment 1 Grade (%s)' % name
        msg['From'] = EMAIL_SENDER
        msg['To'] = email + ', ' + EMAIL_SENDER

        s = smtplib.SMTP(SMTP_SERVER)
        s.starttls()
        s.login(SMTP_USERNAME, SMTP_PASSWORD)
        s.sendmail(EMAIL_SENDER, email + ', ' + EMAIL_SENDER, msg.as_string())
        s.quit()

