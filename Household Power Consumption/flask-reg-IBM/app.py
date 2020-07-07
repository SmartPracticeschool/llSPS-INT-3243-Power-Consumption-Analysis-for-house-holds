from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model = load('svr.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    return render_template('index.html', prediction_text='Global Active Power:  {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
