from flask import Flask,render_template,request,redirect
import json,ast
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/result',methods = ['POST', 'GET'])
def student():
    frm_req = request.form
    handle = frm_req['nme']
    req = requests.get("https://codeforces.com/api/user.info?handles="+handle)
    strr =  ast.literal_eval(json.dumps(req.json()))
    return render_template('profile.html',strr = strr,handle=handle)
    return "<html><body>"+"Happy"+str(strr)+"</body></html>"

if __name__ == '__main__':
   app.run(debug = True)
