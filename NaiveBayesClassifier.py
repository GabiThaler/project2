import pandas as pd

class NaiveBayesClassifier1:
    # בנאי
    def __init__(self,data,target_col ):
        self.df=data
        self.target_col=target_col
        # self.amount_of_columns = self.df.shape[1]
        self.satis_dic ={}
        self.new_df ={}
        self.amount_of_options =None
    # מחלק את הדאטא בייס למילון עם דאטא בייסים חדשים לפי האפשרויות תוצאה
    def deviding_tow_dic(self):
        self.amount_of_Options = self.df[self.target_col].value_counts()
        print(self.amount_of_Options)
        for i in self.amount_of_Options.index:
            self.satis_dic[i] = {}
        print(self.satis_dic)
        for k in self.satis_dic.keys():
            mask = self.df[self.target_col] == k
            filterd =self.df[mask].copy()
            filterd.drop(self.target_col,axis=1,inplace=True)
            self.new_df[k] = filterd
        print(self.new_df)

    #יצירת משתנים של כמות השורות של כל מקרה ובכללי כדי לחשב את הסטיסטיקה
    def amounts(self):
        amount_of_Options1 = {}

        print(self.satis_dic)
        for k in self.satis_dic.keys():
            amount_of_Options1[k] = self.amount_of_Options[k]

    # מכניסים למילון של הסטיסטיקה את כל הסטיסטיקות
    def satiatics(self):
        for i in self.satis_dic.keys():
            for col in self.new_df[i].columns:
                # נוודא שהאבר הספציפי קיים
                if col not in self.satis_dic[i]:
                    self.satis_dic[i][col] = {}

              #נטפל במקרה שלא קיים משהוא אז נחשב לו סטיסטיקה לפי המק
                all_possible_vals = self.df[col].unique()
                for val in all_possible_vals:
                    if val not in self.satis_dic[i][col]:
                        self.satis_dic[i][col][val] = 1 / (self.amount_of_Options[i] + len(all_possible_vals))

                # נעדכן את ההסתברויות לפי הנתונים בפועל
                for k, v in self.new_df[i][col].value_counts().items():
                    self.satis_dic[i][col][k] = v / self.amount_of_Options[i]

        print(self.satis_dic)

    def get_satis_dic(self):
        return self.satis_dic

    def get_new_df(self):
        return self.new_df
