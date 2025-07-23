import  pandas as pd


class Receives_information:

    def __init__(self, dataframe):
        flag=True
        while flag:
            try:
                self.df = pd.read_csv(dataframe)
                flag=False
            except Exception as e:
                print("File not found",e)
                dataframe=input("enter a valid file path")


    def get_data_fraim(self):
        return self.df

