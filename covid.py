import numpy as np
import pickle
import pandas as pd
import uvicorn
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from covid_data import Covid


app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

classifier = joblib.load('finalized_model.sav')

@app.post('/predict_covid')
def predict_covid(data:Covid):
    data = data.dict()
    Breathing_Problem = data['Breathing_Problem']
    Fever = data['Fever']
    Dry_Cough = data['Dry_Cough']
    Sore_throat = data['Sore_throat']
    Running_Nose = data['Running_Nose']
    Headache = data['Headache']
    Hyper_Tension = data['Hyper_Tension']
    Fatigue  = data['Fatigue']
    Gastrointestinal  = data['Gastrointestinal']
    Abroad_travel = data['Abroad_travel']
    Contact_with_COVID_Patient = data['Contact_with_COVID_Patient']
    Attended_Large_Gathering = data['Attended_Large_Gathering']
    Visited_Public_Exposed_Places = data['Visited_Public_Exposed_Places']
    Family_working_in_Public_Exposed_Places = data['Family_working_in_Public_Exposed_Places']
    
    data = [[Breathing_Problem, Fever, Dry_Cough, Sore_throat, Running_Nose, Headache, Hyper_Tension, Fatigue, Gastrointestinal,
             Abroad_travel, Contact_with_COVID_Patient, Attended_Large_Gathering, Visited_Public_Exposed_Places, 
             Family_working_in_Public_Exposed_Places]]
    
    prediction = classifier.predict(data)
    if(prediction[0]>0.5):
        prediction="You have high chances of suffering from Covid"   
    else:
        prediction="Rare chance of suffering from Covid"
    return {'prediction': prediction}

        
        
