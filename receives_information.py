import  pandas as pd


class Receives_information:
    def __init__(self, dataframe):
        self.df = pd.read_csv(dataframe)

    def get_data_fraim(self):
        return self.df
