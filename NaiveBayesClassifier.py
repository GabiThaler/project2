import pandas as pd

class NaiveBayesClassifier:
    # בנאי
    def __init__(self,data,target_col ):
        self.df=data
        self.target_col=target_col
        self.amount_of_columns = self.df.shape[1]
        self.satis_dic ={}
        self.new_df ={}
        # self.amount_of_options
    # מחלק את הדאטא בייס למילון עם דאטא בייסים חדשים לפי האפשרויות תוצאה
    def deviding_tow_dic(self):
        self.amount_of_Options = self.df[self.target_col].value_counts()
        print(self.amount_of_Options)
        for i in self.amount_of_Options.index:
            self.satis_dic[i] = {}

        for k in self.satis_dic.keys():
            mask = self.df[self.target_col] == k
            filterd =self.df[mask].copy()
            filterd.drop(self.target_col,axis=1,inplace=True)
            # print(filterd)
            self.new_df[k] = filterd

    #יצירת משתנים של כמות השורות של כל מקרה ובכללי כדי לחשב את הסטיסטיקה
    def amounts(self):
        amount_of_Options1 = {}

        print(self.satis_dic)
        for k,v in self.satis_dic.items():
            amount_of_Options1[k] = self.amount_of_Options[k].shape[0]
            print(amount_of_Options1[k])


    def satiatics(self):
        pass