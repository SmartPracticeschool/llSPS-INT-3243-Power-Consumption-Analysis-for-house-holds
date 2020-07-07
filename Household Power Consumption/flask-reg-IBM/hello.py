from __future__ import division, print_function
from flask import Flask,request, render_template
from joblib import load
#from werkzeug import secure_filename
#from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import os

app = Flask(__name__)

model= load('svr.save')



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/y_predict', methods=['GET', 'POST'])
def y_predict():
    
    x_test = [[float(x) for x in request.form.values()]]
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    return render_template('index.html', prediction_text='Global Active Power:  {}'.format(output))
    

if __name__ == '__main__':
      port = int(os.getenv('PORT', 8000))
     #app.run(host='0.0.0.0', port=port, debug=True)
      http_server = WSGIServer(('0.0.0.0', port), app)
      http_server.serve_forever()
     #app.run(debug=True)