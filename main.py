# import pandas as pd
# import NaiveBayesClassifier as ne
# import receives_information as ri
from fastapi import FastAPI, HTTPException,Body
from pydantic import BaseModel
import manager
import os
app = FastAPI()

# me =menu.Menu()
# me.menu_manager()

ma = manager.Maneger()

@app.get("/")
def root():
    return {"message": "Welcome to Naive Bayes Classifier API!"}

#מקבל את הנתיב מעלה את הקובץ ומנפה אותו לטבלה
@app.post("/train")
def load_model(data:dict):
    try:
        ma.get_input(data["path"],data["target"])
        ma.set_database()
        ma.trining_database()
        return {"status": "success"}
    except Exception as e:
        return {"status": "failed","message":e}

        # return HTTPException(detail=f"Training failed: {str(e)}")

# נקודת הקצה שמקבלת בקשה מהמשתמש ומחזירה חיזוי
@app.post("/predict")
def predict_user_input(request: dict):
    try:
        prediction_result = ma.calecliting_prediction(request)
        return {"prediction": prediction_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# דף ברירת מחדל פשוט




# @app.get("/predict")
# def example_get():
#     return {
#         "message": "Use POST method to get a prediction.",
#         "example": {
#             "Outlook": "Sunny",
#             "Temperature": "Cool",
#             "Humidity": "High",
#             "Windy": True
#         }
#     }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)




