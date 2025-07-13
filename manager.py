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
        self.path = input("Enter the path of csv file: ")
        a = fr"{self.path}"
        self.target_col = input("Enter the name of target column: ")

    def set_database(self):
        self.RI = receives_information.Receives_information(self.path)
        self.df =self.RI.get_data_fraim()

    def trining_database(self):
        self.nbc = NaiveBayesClassifier.NaiveBayesClassifier1(self.df, self.target_col)
        self.nbc.deviding_tow_dic()
        self.nbc.amounts()
        self.nbc.satiatics()
        self.satis_dic = self.nbc.get_satis_dic()

    #
    # def geting_theinfrmition(self):
    #     print("plese enter the informition")
    #     for i in self.satis_dic:
    #         for j in self.satis_dic[i]:
    #             self.prediction[i]=input(f"Enter the prediction of {i}: ")
    #         break

    def calecliting_prediction(self):
        self.pre = prediction.Prediction(self.df, self.target_col, self.nbc.get_new_df(),self.satis_dic)
        self.pre.get_user_input()
        self.pre.prediction_caliton()
        self.pre.final_calculation()
