from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.Pipeline.predict_pipeline import CustomData,PredictPipeline
application=Flask(__name__)
app=application

#Home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        gender=request.form.get('gender')
        print(gender)
        race_ethnicity=request.form.get('ethnicity').strip() 
        parental_level_of_education=request.form.get('parental_level_of_education')
        lunch=request.form.get('lunch')
        test_preparation_course=request.form.get('test_preparation_course')
        reading_score=float(request.form.get('writing_score'))
        writing_score=float(request.form.get('reading_score'))

        data=CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        # print(f"The data is {data.values()}")
        custom_data_input_dict = {
                "gender": [gender],
                "race_ethnicity": [race_ethnicity],
                "parental_level_of_education": [parental_level_of_education],
                "lunch": [lunch],
                "test_preparation_course": [test_preparation_course],
                "reading_score": [reading_score],
                "writing_score": [writing_score],
            }
        pred_df=pd.DataFrame(custom_data_input_dict)
        # pred_df=data.get_data_as_frame()
        # print(pred_df)
        print(pred_df)
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=str(results[0]))
    
if __name__=="__main__":
    app.run(host='0.0.0.0')    