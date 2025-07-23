# from typing_inspection.typing_objects import target

import receives_information
import NaiveBayesClassifier
import prediction



class Maneger:
    def __init__(self):
        self.path =None
        self.df = None
        self.RI =None
        self.satis_dic = None
        self.prediction={}
        self.prediction_result={}

    def get_input(self):
        # self.path = input("Enter the path of csv file: ")
        # a = fr"{self.path}"
        # self.target_col = input("Enter the name of target column: ")
        self.path=fr"C:\Users\gmth0\OneDrive\Pictures\Screenshots\PlayTennis.csv"
        self.target_col="PlayTennis"

    def set_database(self):
        self.RI = receives_information.Receives_information(self.path)
        self.df =self.RI.get_data_fraim()
        while(self.target_col not in self.df):
            self.target_col = input("Enter the name of a valid target column: ")

    def trining_database(self):
        self.nbc = NaiveBayesClassifier.NaiveBayesClassifier1(self.df, self.target_col)
        self.nbc.deviding_tow_dic()
        self.nbc.amounts()
        self.nbc.satiatics()
        self.satis_dic = self.nbc.get_satis_dic()



    def calecliting_prediction(self):
        self.pr= prediction.Prediction(self.df, self.target_col, self.nbc.get_new_df(),self.satis_dic)
        self.pr.get_user_input()
        self.pr.prediction_caliton()
        self.pr.final_calculation()
