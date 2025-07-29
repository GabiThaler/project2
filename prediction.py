import pandas as pd


class Prediction:
    def __init__(self,model):
        self.prediction={}
        self.prediction_result={}
        self.model=model


    def get_user_input(self):
        print("Please enter the input data:")
        for col in self.model["col"]:
            if col != self.model["target_col"]:
                val = input(f"Enter value for '{col}': ")
                # המרה לבוליאני אם צריך
                if val.lower() == 'true':
                    val = True
                elif val.lower() == 'false':
                    val = False
                self.prediction[col] = val

    def prediction_caliton(self):
        for i in self.model:
            if i not in ["col","target_col","amount_of_col"]:
                flag =True
                for col in self.model["col"]:
                    if col != self.model["target_col"]:
                        if flag:
                            self.prediction_result[i] = self.model[i][col][self.prediction[col]]
                            flag=False

                        else:
                            self.prediction_result[i] *= self.model[i][col][self.prediction[col]]

                self.prediction_result[i] *= self.model["amount_of_col"][i] / self.model["amount_of_col"]["all"]
        print(self.prediction_result)

    def final_calculation(self):
        max =0
        result =None
        for k,v in self.prediction_result.items():
            if v> max:
                max=v
                result=k
        print(f"The most likely outcome {result}")
