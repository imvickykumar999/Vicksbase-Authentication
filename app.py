
from datetime import datetime
from bson.json_util import dumps
import requests, os
from bs4 import BeautifulSoup as bs
from werkzeug.utils import secure_filename
from flask import Flask, flash, jsonify, url_for, session, request, redirect, render_template, send_from_directory

txt = open('hideme.txt', "r")
txtread = txt.read().strip()
print(txtread, type(txtread))

try:
    os.mkdir('static/uploads')
except Exception as e:
    print(e)
    pass

app = Flask(__name__)

@app.route("/")
def yourquotes():
    from vicks import crud
    obj1 = crud.vicks('@Hey_Vicks')

    data = obj1.pull()

    if data == None:
        obj1.push()

    data = obj1.pull()
    print('------------------------->', data)
    return render_template("yourquotes.html",
                           data = data,
                           )


@app.route('/converted_yourquotes', methods=['POST'])
def converted_yourquotes():
    from vicks import crud

    credentials = request.form['credentials']
    if credentials != '@Hey_Vicks':
        return render_template("404.html", message = 'Wrong Credentials')

    person = request.form['person']

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
    return render_template("yourquotes.html",
                           data = data,
                           )

if __name__ == '__main__':
    app.run(debug=True)
