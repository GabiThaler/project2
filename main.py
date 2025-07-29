import pandas as pd
import triner as ne
import receives_information as ri
import fastapi
import menu



app = fastapi.FastAPI()


me =menu.Menu()
me.menu_manager()
# #מהתחל את הapi
# @app.get("/")
# def root():
#     return {"message": "Welcome to Naive Bayes Classifier API!"}
#
# # #מאמן את המודל
# # @app.post("/train")
# # def train():

