{"filter":false,"title":"app.py","tooltip":"/flask-forms/app.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":38},"action":"remove","lines":["from flask import Flask, render_template, request, redirect, url_for","import os","","app = Flask(__name__)","","# the default is the GET method","@app.route('/countries')","def index():","    return {","        \"sg\":\"Singapore\",","        \"my\" : \"Malaysia\",","        \"cn\" : \"China\"","    }","    ","@app.route('/')","def test_index():","    return render_template('api.html')"],"id":2},{"start":{"row":0,"column":0},"end":{"row":15,"column":22},"action":"insert","lines":["from flask import Flask, render_template, request, redirect, url_for","import os","","app = Flask(__name__)","","msg = []","","@app.route('/')","def index():","\treturn render_template('index.template.html', messages = msg)","","@app.route('/', methods=['POST'])","def add_message():","  new_message = request.form['new-message']","  msg.append(new_message)","  return redirect('/')"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":22},"end":{"row":15,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1571019017511,"hash":"edb54ee70cc0bfc566df7575fddcb950d0e5cd58"}