from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.get("/")
def hello_world():
    return render_template("index.html")

@app.get("/apply.html")
@app.get("/apply")
def apply():
    return render_template("apply.html")

@app.post("/predict")
def predict():
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    dependents = int(request.form['dependents'])
    education = int(request.form['education'])
    employed = int(request.form['employed'])
    income = int(request.form['income'])
    coincome = int(request.form['coincome'])
    loan_amount = int(request.form['loan_amount'])
    loan_term = int(request.form['loan_term'])
    credhist = int(request.form['credhist'])
    property = int(request.form['property'])
    score = int(request.form['score'])
    predicted = model.predict([[gender, married, dependents, education, employed, income, coincome, loan_amount, loan_term, credhist, property, score]])
    
    if (predicted[0] == 0):
        return render_template("index.html", prediction_text="no loan can be granted")
    else :
        return render_template("index.html", prediction_text="loan can be granted")

if __name__ == "__main__":
    app.run(debug=True)