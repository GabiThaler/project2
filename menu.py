from manager import Maneger
class Menu:
    def __init__(self):
        self.me= Maneger()

    def menu_manager(self):
        flag =True
        while flag:
            self.vew_menu()
            choice=input()
            match choice:
                    case "1":
                        self.me.get_input()
                        self.me.set_database()
                        self.me.trining_database()
                    case "2":
                        self.me.calecliting_prediction()


                    case "0":
                        flag =False





    def vew_menu(self):
        print("Welcome to Naive Bayes Classifier")
        print("plase enter youer coice")
        print("to enter a new data base enter 1")
        print("to enter data for prediction enter 2")
        print("to exit enter 0")