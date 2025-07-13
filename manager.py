import receives_information
import NaiveBayesClassifier
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
    #             self.prediction[i]=input("Enter the prediction of {i}: ")
    #         break

    def get_user_input(self):
        print("Please enter the input data:")
        for col in self.df.columns:
            if col != self.target_col:
                val = input(f"Enter value for '{col}': ")
                # המרה לבוליאני אם צריך
                if val.lower() == 'true':
                    val = True
                elif val.lower() == 'false':
                    val = False
                self.prediction[col] = val

    def prediction_caliton(self):
        for i in self.satis_dic:
            flag =True
            for col in self.df.columns:
                if col != self.target_col:
                    if flag:
                        self.prediction_result[i] = self.satis_dic[i][col][self.prediction[col]]
                        flag=False

                    else:
                        self.prediction_result[i] *= self.satis_dic[i][col][self.prediction[col]]

        print(self.prediction_result)

    # def final_calcliton(self):
    #     for i in self.satis_dic:
    #         for col in self.df.columns:
    #             if col != self.target_col:
    #
