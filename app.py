import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder="D:/data science/Hr_Analyst/templates")
model_path = "D:/data science/Hr_Analyst/notebooks/data/model.pkl"
model = pickle.load(open(model_path,'rb'))  # Corrected to use the variable

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output =(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee status is $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)


