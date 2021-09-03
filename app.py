
from bson.json_util import dumps
import requests, os
from flask import Flask, request, render_template

txt = open('hideme.txt', "r")
txtread = txt.read().strip()
print(txtread, type(txtread))

try:
    os.mkdir('static/uploads')
except Exception as e:
    print(e)
    pass

app = Flask(__name__)

# https://myaccount.google.com/u/3/lesssecureapps?pli=1&rapt=AEjHL4MpjjYh8Z-01vJ5GRsQXICYQsXHG0PweSjWenlbAJfes6qNKbHKs_CfCVh0d5qUO58qFeeB0sYCbA3GANLf-965469dVA

@app.route("/vicksmail")
def vicksmail():
    return render_template("mailsent.html", sent='no')

@app.route("/mail_sent", methods=['POST'])
def mail_sent():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "sagar.sws2000@gmail.com"
    toaddr = request.form['credentials']

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "Vicks OTP"
    import random
    otp = str(random.randint(1000,9999))
    # otp = '7639'

    file1 = open("otp.txt", "w")
    file1.write(otp)
    file1.close()

    body = f'''\
<html>
  <head>Vicks OTP</head>
  <body>
    <p>Hi !<br>
       How are you?<br>
       Here is the OTP = {otp} you wanted.
    </p>
  </body>
</html>
    '''
    msg.attach(MIMEText(body, 'html'))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "pythonsagarvicky")

    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
    return render_template("mailsent.html", sent='yes')

@app.route("/")
def vicksbase():
    from vicks import crud
    obj1 = crud.vicks('@Hey_Vicks')

    data = obj1.pull()

    if data == None:
        obj1.push()

    data = obj1.pull()
    print('------------------------->', data)
    return render_template("vicksbase.html",
                           data = data,
                           )


@app.route('/converted_vicksbase', methods=['POST'])
def converted_vicksbase():
    from vicks import crud

    credentials = request.form['credentials']
    person = request.form['person']
    otp = request.form['otp']

    if credentials != '@Hey_Vicks':
        return render_template("404.html", message = 'Wrong Credentials')

    f=open("otp.txt",'r')
    getotp = f.read().strip()
    f = open("otp.txt", "w")
    f.write('-')
    f.close()

    if otp == getotp and otp != '-':
        if person == '':
            obj1 = crud.vicks(credentials)
        else:
            obj1 = crud.vicks(credentials, child = person)

        message = f'''
        {request.form['message']}
        '''
        if message == '':
            obj1.push()
        else:
            obj1.push(message)

        data = obj1.pull()
        print('------------------------->', data)
        return render_template("vicksbase.html",
                               data = data,
                               )
    else:
        return render_template("404.html", message = 'Wrong OTP')

if __name__ == '__main__':
    app.run(debug=True)
