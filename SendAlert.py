import smtplib
from email.mime.text import MIMEText


def sendAlert(stock):
    url = "https://api.iextrading.com/1.0/stock/";
    # response = req.get(url + stock + "/news")
    # print(response)
    your_email = '<your_email>'
    msg_content = url+stock+"/news"
    message = MIMEText(msg_content, 'html')
    message['From'] = 'Auto Trader'+your_email
    message['To'] = 'Client Name'+your_email
    # message['Cc'] = 'Receiver2 Name <receiver2@server>'
    message['Subject'] = 'Stock Alert for - '+stock
    msg_full = message.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(your_email, "<your_password>")
    server.sendmail(your_email, your_email, msg_full)
    server.quit()

