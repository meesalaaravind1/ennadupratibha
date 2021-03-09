from flask import Flask,request
import pandas as pd
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as bsp

app= Flask(__name__)

def sourceCode(url):
  html = urlopen(url)
  return (bsp(html.read(), 'html.parser'))

@app.route('/query_example')
def query_example():
    return ("flaskapp")

@app.route('/form_example',methods=["POST","GET"])
def form_example():
    if request.method == 'POST':
        link=request.form.get('link')
        bs=sourceCode(link)
        s=""
        for i in bs.find_all('p'):
            s+=(i.text)+"<br>"
        # print (s)
        return ('''<form method="POST" >
    Website <input type="text" name="link">
    <input type="submit">
    </form>
    '''+'\n'+
    s)
    return '''<form method="POST" >
    Website <input type="text" name="link">
    <input type="submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True,port=5000)
