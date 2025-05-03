# -*- coding: utf-8 -*-

# Library imports
from fastapi import FastAPI # for creating api in python 
import uvicorn # for running the ASGI 
import pandas as pd # for data manipulation and analysis
import pickle # for loading the model
import json # for converting data to json format
import numpy as np # for numerical operations 
from bank import Bankinputdata # assuming Bank is a module containing the model
   
app = FastAPI() # creating an instance of fastapi app

with open('tree_Accuracy_based.pkl', 'rb') as f: #loading model file
    model = pickle.load(f)

@app.get('/') # defining home endpoint
def index():
    return {'message': 'Welcome to the Bank Loan Prediction API!'}  

# @app.post('/name') # defining name endpoint
# def get_name(name: str):
#     return {'message': f'Hello, {name}!'}

@app.post('/credit_risk_predictor') # defining prediction endpoint
def Bank_pred(data: Bankinputdata): # idher data ko model pydantic se validate kiya gaya hai 
    
    # Convert the input data to a DataFrame
    input_data = data.json()
    data = json.loads(input_data)

    # Manually doing so :-- 
    Age = data['Age']
    Sex = data['Sex']
    Job = data['Job']
    Housing = data['Housing']
    Saving_accounts = data['Saving_accounts']
    Checking_account = data['Checking_account']
    Credit_amount = data['Credit_amount']
    Duration = data['Duration']
    Purpose_car = data['Purpose_car']
    Purpose_domestic_appliances = data['Purpose_domestic_appliances']
    Purpose_education = data['Purpose_education']
    Purpose_furniture_equipment = data['Purpose_furniture_equipment']
    Purpose_radio_TV = data['Purpose_radio_TV']
    Purpose_repairs = data['Purpose_repairs']
    Purpose_vacation_others = data['Purpose_vacation_others']
    
    # Make predictions using the loaded model
    Predictions = model.predict([[Age,Sex,Job,Housing,Saving_accounts,Checking_account,Credit_amount,Duration,Purpose_car,Purpose_domestic_appliances,Purpose_education,Purpose_furniture_equipment,Purpose_radio_TV,Purpose_repairs,Purpose_vacation_others]])
   
    if Predictions[0] == 1:
        result = 'Good '
    else:
        result = 'Bad '       
        
    return {'Prediction': result} # returning the prediction as a response
   
# 5.Run the app using uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000) 
