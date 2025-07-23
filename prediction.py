import pandas as pd


class Prediction:
    def __init__(self,df,target_col,new_df,satistic_dic):
        self.prediction={}
        self.prediction_result={}
        self.df=df
        self.target_col=target_col
        self.new_df=new_df
        self.satis_dic=satistic_dic



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
            for col in self.df.columns:
                flag = True
                if col != self.target_col:
                    if flag:
                        self.prediction_result[i] = self.satis_dic[i][col][self.prediction[col]]
                        flag=False
                    else:
                        self.prediction_result[i] *= self.satis_dic[i][col][self.prediction[col]]

            self.prediction_result[i] *= self.new_df[i].shape[0] / self.df.shape[0]
        print(self.prediction_result)

    def final_calculation(self):
        max =0
        result =None
        for k,v in self.prediction_result.items():
            if v> max:
                max=v
                result=k
        return  f"The most likely outcome {result}"
