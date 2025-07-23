# import pandas as pd
# import NaiveBayesClassifier as ne
# import receives_information as ri
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import manager
import os
app = FastAPI()

# me =menu.Menu()
# me.menu_manager()

ma = manager.Maneger()
#מקבל את הנתיב מעלה את הקובץ ומנפה אותו לטבלה
@app.on_event("startup")
def load_model():
    ma.get_input()
    ma.set_database()
    ma.trining_database()


#מבנה הקלט של המשתמש
class PredictionRequest(BaseModel):
    Outlook: str
    Temperature: str
    Humidity: str
    Windy: bool


# נקודת הקצה שמקבלת בקשה מהמשתמש ומחזירה חיזוי
@app.post("/predict")
def predict_user_input(request: PredictionRequest):
    try:
        input_data = request.dict()
        prediction_result = ma.calecliting_prediction(input_data)
        return {"prediction": prediction_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# דף ברירת מחדל פשוט
@app.get("/")
def root():
    return {"message": "Welcome to Naive Bayes Classifier API!"}



@app.get("/predict")
def example_get():
    return {
        "message": "Use POST method to get a prediction.",
        "example": {
            "Outlook": "Sunny",
            "Temperature": "Cool",
            "Humidity": "High",
            "Windy": True
        }
    }







