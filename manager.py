# from typing_inspection.typing_objects import target

from receives_information import Receives_information
from trainer import Trainer
from classifier import Classifier



class Maneger:
    def __init__(self):
        self.path =None
        self.df = None
        self.model = None
        self.prediction={}
        self.prediction_result={}
        self.coles=None
        self.pr=None

    def get_input(self, path, target_col):
        self.path = path
        self.target_col = target_col


    def set_database(self):
        RI = Receives_information(self.path)
        self.df =RI.get_data_fraim()
        while(self.target_col not in self.df):
            self.target_col = input("Enter the name of a valid target column: ")



    def trining_database(self):
        self.nbc = Trainer(self.df, self.target_col)
        self.nbc.deviding_tow_dic()
        self.nbc.amounts()
        self.nbc.satiatics()
        self.model = self.nbc.get_satis_dic()
        self.model["target col"] = self.target_col
        self.model["colmes"] = self.df.columns.tolist()
        self.model["amount off aptions"] = self.nbc.get_amount_of_options()

        print(self.model)




    def calecliting_prediction(self,user_input):
        self.pr= Classifier(self.model)
        # self.pr.get_user_input()
        self.pr.prediction_caliton(user_input)
        return self.pr.final_calculation()
