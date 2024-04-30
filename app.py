from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData,PredictPipline

application =Flask(__name__)

#creating a variable to create the application

app=application
#creating a route for the home page

@app.route('/')
def index():
    return render_template('index.html')

#route the application to the page that  accepts prediction parameters
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            test_preparation_course=request.form.get('test_preparation_course'),
            lunch=request.form.get('lunch'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))

        )

        #convert the predict data to data frome by cal=lin the function responsible
        pred_df=data.get_data_as_dataframe()
        print(pred_df)

        #initialize the predict pipeline
        predic_pipeline=PredictPipline()
        results= predic_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])
    
    #to run app.py
if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)