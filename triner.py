import pandas as pd

class Triner:
    # בנאי
    def __init__(self,data,target_col ):
        self.df=data
        self.target_col=target_col
        self.amount_of_columns = self.df.shape[0]
        self.model ={}
        self.new_df ={}
        self.amount_of_options =None
        self.amount_of_options1 = {}
    # מחלק את הדאטא בייס למילון עם דאטא בייסים חדשים לפי האפשרויות תוצאה
    def deviding_tow_dic(self):
        print(self.df)
        self.amount_of_Options = self.df[self.target_col].value_counts()
        print(self.amount_of_Options)
        for i in self.amount_of_Options.index:
            self.model[i] = {}
        print(self.model)
        for k in self.model.keys():
            mask = self.df[self.target_col] == k
            filterd =self.df[mask].copy()
            filterd.drop(self.target_col,axis=1,inplace=True)
            self.new_df[k] = filterd
        print(self.new_df)

    #יצירת משתנים של כמות השורות של כל מקרה ובכללי כדי לחשב את הסטיסטיקה
    def amounts(self):

        print(self.model)
        for k in self.model.keys():
            self.amount_of_options1[k] = int(self.amount_of_Options[k])
        self.amount_of_options1["all"] = self.amount_of_columns
        print("amount ",self.amount_of_options1)


    # מכניסים למילון של הסטיסטיקה את כל הסטיסטיקות
    def satiatics(self):
        for i in self.model.keys():
            for col in self.new_df[i].columns:
                # נוודא שהאבר הספציפי קיים
                if col not in self.model[i]:
                    self.model[i][col] = {}

              #נטפל במקרה שלא קיים משהוא אז נחשב לו סטיסטיקה לפי המק
                all_possible_vals = self.df[col].unique()
                for val in all_possible_vals:
                    if val not in self.model[i][col]:
                        self.model[i][col][val] = 1 / (self.amount_of_Options[i] + len(all_possible_vals))

                # נעדכן את ההסתברויות לפי הנתונים בפועל
                for k, v in self.new_df[i][col].value_counts().items():
                    self.model[i][col][k] = v / self.amount_of_Options[i]
        self.model["amount_of_col"] = self.amount_of_options1
        self.model["target_col"] = self.target_col
        print("df",self.df.columns)
        self.model["col"] = self.df.columns.tolist()


        print(self.model)

    def get_features(self):
        features={}
        for i in  self.df.columns:
            features[i] = self.df[i].unique()
        return features



    def get_satis_dic(self):
        return self.model

    def get_new_df(self):
        return self.new_df
