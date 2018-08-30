import poplib

username = "2027665022@qq.com"
password = "xhqqwasd123789"

mail_server = "mail.csvt.net"

p = poplib.POP3(mail_server)
p.usr(username)

