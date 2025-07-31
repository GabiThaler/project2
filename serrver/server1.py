import fastapi
import numpy as np
from managing_project import manager
from fastapi import HTTPException
from pydantic import BaseModel


#מאמן את המודל מיד
app = fastapi.FastAPI()
maniger= manager.Maneger()
maniger.set_database()
maniger.trining_model()



# me =menu.Menu()
# me.menu_manager()


# הגדר מחלקת קלט
class UserInput(BaseModel):
    Outlook: str
    Temperature: str
    Humidity: str
    Windy: bool

#הנתיב הבסיסי
@app.get("/")
def root():
    return {"message": "Welcome to Naive Bayes Classifier API!"}

#נתיב שמחזיר את כל האפשרויות בכל פיצר
@app.get("/get_features")
def get_features():
    raw_features = maniger.features()

    # המרה לסוגים פשוטים
    def clean(obj):
        if isinstance(obj, dict):
            return {clean(k): clean(v) for k, v in obj.items()}
        elif hasattr(obj, "tolist"):
            return obj.tolist()
        elif isinstance(obj, (np.integer, np.int64, np.int32)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float64, np.float32)):
            return float(obj)
        elif isinstance(obj, (np.bool_)):
            return bool(obj)
        else:
            return obj

    safe_features = clean(raw_features)
    return safe_features






# נקרא לפונקציה שכבר קיימת אצלך
@app.post("/predict")
def predict_route(user_input: UserInput):
    try:


        # חישוב חיזוי
        result = maniger.calecliting_prediction(user_input.dict())



        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


