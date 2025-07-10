import  pandas as pd


class receives_information:
    df = pd.DataFrame()
    def __init__(self, dataframe):
        self.df = pd.read_csv(dataframe)

    def get_data_fraim(self):
        return self.df
