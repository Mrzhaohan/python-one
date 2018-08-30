import smtplib
mail_server = "localhost"
mail_port = 25
from_addr = '2027665022@qq.com'
to_addr = '1121697499@qq.com'

from_header = 'From : %s\r\n' % from_addr
toheader = "Tp : %s\r\n" % to_addr
subject_header = 'Suject: tset!!'

body = 'This is  a test mail'

email_message = "%s\n%s\n%s\n%s\n" % (from_header, to_header, subject_header, body)
s.smtplib.SMTP(mail_server, mail_server_port)
s.sendmail(from_addr, to_addr, email_message)
s.quit()
