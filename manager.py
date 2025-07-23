# from typing_inspection.typing_objects import target

from receives_information import Receives_information
from trainer import Trainer
from classifier import Classifier



class Maneger:
    def __init__(self):
        self.path =None
        self.df = None
        self.satis_dic = None
        self.prediction={}
        self.prediction_result={}
        self.coles=None

    def get_input(self,path,target="PlayTennis"):
        a = fr"{path}"
        self.path = a
        self.target_col = target

    def set_database(self):
        RI = Receives_information(self.path)
        self.df =RI.get_data_fraim()
        while(self.target_col not in self.df):
            self.target_col = input("Enter the name of a valid target column: ")
        self.coles = self.df.columns.tolist()


    def trining_database(self):
        self.nbc = Trainer(self.df, self.target_col)
        self.nbc.deviding_tow_dic()
        self.nbc.amounts()
        self.nbc.satiatics()
        self.satis_dic = self.nbc.get_satis_dic()



    def calecliting_prediction(self,user_input):
        self.pr= Classifier(self.df, self.target_col, self.nbc.get_new_df(),self.satis_dic,user_input)
        # self.pr.get_user_input()
        self.pr.prediction_caliton()
        return self.pr.final_calculation()
