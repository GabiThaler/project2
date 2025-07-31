from data import receives_information
from training_model import triner
from classifier import prediction


class Maneger:
    def __init__(self):
        self.path = r'C:\Users\gmth0\OneDrive\Pictures\Screenshots\PlayTennis.csv'
        self.df = None
        self.RI =None
        self.model = None
        self.prediction={}
        self.prediction_result={}
        self.target_col ="PlayTennis"
        self.trian_model =None

    def set_database(self):
        self.RI = receives_information.Receives_information(self.path)
        self.df =self.RI.get_data_fraim()


    def trining_model(self):
        self.trian_model = triner.Triner(self.df, self.target_col)
        self.trian_model.deviding_tow_dic()
        self.trian_model.amounts()
        self.trian_model.satiatics()
        self.model = self.trian_model.get_satis_dic()



    def calecliting_prediction(self, user_input):
        self.pre = prediction.Prediction(self.model, user_input)
        # self.pre.get_user_input()
        self.pre.prediction_caliton()
        return self.pre.final_calculation()


    def features(self):
        return self.trian_model.get_features()