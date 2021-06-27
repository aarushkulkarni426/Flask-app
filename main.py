from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)

@app.route('/')
def home():
 return render_template('main.html')

@app.route('/ask_question', methods=['GET', 'POST'])
def ask_question():
  if request.method == "POST":
    global question 
    question = request.form['question']
    _request = requests.get(f'https://api.wolframalpha.com/v2/query?input={question}&appid=VWT5QG-JXX4KQAKAA&output=json')
    _json = _request.json()
    answer=_json['queryresult']['pods'][1]['subpods'][0]['plaintext']
    print(answer) 
    return answer
  else: 
    return render_template("ask_question.html")

@app.route('/tutoring',methods=['GET', 'POST'])
def tutor():
  _question=request.form.get('question')
  _request = requests.get(f'https://api.wolframalpha.com/v2/query?input={question}&appid=VWT5QG-JXX4KQAKAA&output=json')
  _json = _request.json()
  answer=_json['queryresult']['pods'][1]['subpods'][0]['plaintext']
  print(answer)
  return f"<h1>{answer}</h1>"
@app.route('/vaccines')
def vaccines():
  return render_template('vaccines.html')

app.run(host='0.0.0.0', port=8080)