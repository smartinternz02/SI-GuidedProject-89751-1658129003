from flask import Flask, render_template, request
import numpy as np
import pickle
import os
import pandas
app = Flask(__name__)
model = pickle.load(open (r'rdf.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict')
def predict():
    return render_template('predict.html')
@app.route('/submit', methods=[ "POST", "GET"])
def submit():    
    input_feature=[int (x) for x in request.form.values() ]
    input_feature=[np.array(input_feature)]
    print(input_feature)
    names = ['Gender', 'Married', 'Dependents', 'Education', 'Self Employed', 'ApplicantIncome' , 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']   
    data = pandas.DataFrame(input_feature, columns=names)
    print(data)
    prediction=model.predict(data)
    print (prediction)
    prediction = int(prediction)   
    print(type(prediction))
    if (prediction == 0):
        return render_template("output.html", result = "Loan wil Not be Approved")
    else:
        return render_template("output.html",result = "Loan will be Approved")
if __name__ == '__main__':
    app.run(debug = True)