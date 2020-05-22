import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
# Setup
email = EmailMessage()
email['from'] = 'Romeo Enso'
email['to'] = 'joyanne_1610@yahoo.com'
email['subject'] = 'Happy Anniversary'

email.set_content(html.substitute({'name': 'Mahal ko!'}), 'html')

# setup the smtp server
# check your gmail to allow security apps
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('romeo.enso93@gmail.com', 'rmemeo584')
  smtp.send_message(email)
  print('all good')