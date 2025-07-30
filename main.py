import pandas as pd
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import triner as ne
import receives_information as ri
import fastapi
import numpy as np
import menu
import manager


#מאמן את המודל מיד
app = fastapi.FastAPI()
maniger=manager.Maneger()
maniger.set_database()
maniger.trining_model()



# me =menu.Menu()
# me.menu_manager()
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



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001)
