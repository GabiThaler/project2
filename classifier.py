import pandas as pd


class Classifier:
    def __init__(self,model):
        self.model = model
        self.prediction_result = {}


    def prediction_caliton(self,user_input):
        for i in self.model:
            if i not in ["target col", "colmes", "amount off aptions"]:
                flag = True
                for col in self.model["colmes"]:
                    if (not(col == self.model["target col"])):
                        if flag:
                            self.prediction_result[i] = self.model[i][col][user_input[col]]
                            flag=False
                        else:
                            self.prediction_result[i] *= self.model[i][col][user_input[col]]


                self.prediction_result[i] *= self.model["amount off aptions"][i] / self.model["amount off aptions"]["all"]
        print(self.prediction_result)

    def final_calculation(self):
        max =0
        result =None
        for k,v in self.prediction_result.items():
            if v > max:
                max=v
                result=k
        return  f"The most likely outcome {result}"





    #
    # def get_user_input(self):
    #     print("Please enter the input data:")
    #     for col in self.df.columns:
    #         if col != self.target_col:
    #             val = input(f"Enter value for '{col}': ")
    #             # המרה לבוליאני אם צריך
    #             if val.lower() == 'true':
    #                 val = True
    #             elif val.lower() == 'false':
    #                 val = False
    #             self.prediction[col] = val

