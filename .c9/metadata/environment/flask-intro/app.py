{"filter":false,"title":"app.py","tooltip":"/flask-intro/app.py","undoManager":{"mark":70,"position":70,"stack":[[{"start":{"row":0,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["from flask import Flash, render_template, request, redirect, url_for","import os","","app = Flask(__name__)","<--top-->","<--bottom-->","#’magic code” -- boilerplate","if __name__ == ‘__main__’:","app.run(host=os.environ.get(‘IP’),","port=int(os.environ.get (‘PORT’),","debug=True)",""],"id":1}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":12},"action":"remove","lines":["<--top-->","<--bottom-->"],"id":2}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["‘"],"id":3}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["'"],"id":4}],[{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["’"],"id":5}],[{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["'"],"id":6}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"remove","lines":["‘"],"id":7}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["'"],"id":8}],[{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"remove","lines":["’"],"id":9}],[{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["'"],"id":10}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["’"],"id":11}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["'"],"id":12}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["‘"],"id":13}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["'"],"id":14}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "],"id":15}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "],"id":16}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":17}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":18}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"remove","lines":["’"],"id":19}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":[" "],"id":20},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["'"]}],[{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"remove","lines":["'"],"id":21}],[{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["\""],"id":22}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["”"],"id":23}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["\""],"id":24}],[{"start":{"row":4,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["def hello():","\tname=”Paul”","\treturn render_template(‘index.template.html, first_name=name’)",""],"id":25}],[{"start":{"row":6,"column":63},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":26}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["\\"],"id":27}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["\\"],"id":28}],[{"start":{"row":3,"column":21},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":29}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":12},"action":"remove","lines":["”Paul”"],"id":30},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["\""]}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["D"],"id":31},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["i"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["y"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["a"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["n"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["a"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["h"]}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["\""],"id":32}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":[" "],"id":33}],[{"start":{"row":7,"column":61},"end":{"row":7,"column":62},"action":"remove","lines":["’"],"id":34}],[{"start":{"row":7,"column":61},"end":{"row":7,"column":62},"action":"insert","lines":["'"],"id":35}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"remove","lines":["‘"],"id":36}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["'"],"id":37}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":38}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":16},"action":"insert","lines":["@app.route(‘/’) "],"id":39}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["’"],"id":40}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":15},"action":"insert","lines":["''"],"id":41}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"remove","lines":["‘"],"id":42}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["'"],"id":43}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"remove","lines":["'"],"id":44}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":8},"action":"remove","lines":["ell"],"id":45}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["o"],"id":46}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["h"],"id":47}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["i"],"id":48},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["n"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["d"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["e"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["x"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":49},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":50},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["# \"magic code\" -- boilerplate","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get ('PORT'),","            debug=True)",""],"id":51},{"start":{"row":10,"column":0},"end":{"row":14,"column":23},"action":"insert","lines":["# \"magic code\" -- boilerplate","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":8,"column":63},"action":"remove","lines":["from flask import Flash, render_template, request, redirect, url_for","import os","","app = Flask(__name__)","","@app.route('/') ","def index():","\tname= \"Diyanah\"","\treturn render_template('index.template.html, first_name=name')"],"id":52},{"start":{"row":0,"column":0},"end":{"row":9,"column":68},"action":"insert","lines":["from flask import Flask, render_template, request, redirect, url_for","import os","","app = Flask(__name__)","","# routing is the process mapping an URL to a function","@app.route('/')","def hello():","    name = \"Paul\"","    return render_template('index.template.html', first_name = name)"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":53},"action":"remove","lines":["# routing is the process mapping an URL to a function"],"id":53},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":16},"action":"remove","lines":["Paul"],"id":54},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["D"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["i"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["y"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["a"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["n"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["a"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["h"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":68},"action":"remove","lines":["return render_template('index.template.html', first_name = name)"],"id":55},{"start":{"row":8,"column":4},"end":{"row":8,"column":68},"action":"insert","lines":["return render_template('index.template.html', first_name = name)"]}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"remove","lines":["from flask import Flask, render_template, request, redirect, url_for","import os","","app = Flask(__name__)","","@app.route('/')","def hello():","    name = \"Diyanah\"","    return render_template('index.template.html', first_name = name)","","# \"magic code\" -- boilerplate","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":56},{"start":{"row":0,"column":0},"end":{"row":15,"column":23},"action":"insert","lines":["from flask import Flask, render_template, request, redirect, url_for","import os","","app = Flask(__name__)","","# routing is the process mapping an URL to a function","@app.route('/')","def hello():","    name = \"Paul\"","    return render_template('index.template.html', first_name = name)","","# \"magic code\" -- boilerplate","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":16},"action":"remove","lines":["Paul"],"id":57},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["D"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["i"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["y"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["a"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["n"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["a"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["h"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":53},"action":"remove","lines":["# routing is the process mapping an URL to a function"],"id":58},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":68},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":59},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":60},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":10,"column":4},"end":{"row":11,"column":0},"action":"insert","lines":["",""]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "],"id":62},{"start":{"row":10,"column":4},"end":{"row":11,"column":0},"action":"remove","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":63},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":64}],[{"start":{"row":10,"column":0},"end":{"row":13,"column":68},"action":"insert","lines":["@app.route('/')","def hello():","    name = \"Diyanah\"","    return render_template('index.template.html', first_name = name)"],"id":65}],[{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["a"],"id":66},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["b"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["o"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["u"]},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["t"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["-"]}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"remove","lines":["-"],"id":67}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":9},"action":"remove","lines":["hello"],"id":68},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["a"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["b"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["o"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["u"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":28},"end":{"row":13,"column":33},"action":"remove","lines":["index"],"id":69},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["a"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["b"]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["o"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["u"]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":20},"action":"remove","lines":["    name = \"Diyanah\""],"id":71},{"start":{"row":11,"column":12},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":48},"end":{"row":12,"column":67},"action":"remove","lines":[", first_name = name"],"id":72}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":49},"end":{"row":12,"column":49},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1570598141303,"hash":"cdd033d3d31f6af98a5b49bb1a259edef162b065"}