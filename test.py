import yagmail
yag = yagmail.SMTP(user='xuyahe@126.com', password='xuyahe123', host='smtp.126.com')
yag.send(['337467239@qq.com','842917055@qq.com'],'this is a mail from xuyahe', 'hello world')
