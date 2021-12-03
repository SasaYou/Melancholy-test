# coding:utf-8
from flask import Flask, render_template , request
import Qdate
from question import Qtotal

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('top.html')


@app.route("/strt")
def strt():
    return render_template('question.html',qs=Qdate.qs)

@app.route("/ans")
def anser():
    total = 0
    q_name=[]
    for x in range(1,21):
        q_name.append(str(x)+"q")
    for y in q_name:
        value = request.args.get(y)
        if value is None: return render_template('returts.html')
        score= Qtotal.get_score(y,int(value))
        total += score

    return render_template('answer.html',total=total)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    
