
class Pupil:    
    def __init__(self, name, weight_initial, weight_final):
        self.name = name
        self.weight_initial = weight_initial
        self.weight_final = weight_final

    def store_name(self):
         
         return self.name

    def isvalid_weight_initial(self):

        if self.weight_initial.isdigit():
            self.weight_initial = int(self.weight_initial)
            if 50 <= self.weight_initial <= 80:
                return self.weight_initial
            else:
                print("Invalid initial weight. (50-80kg) Rerun program")
                return False
        else:
            print("Enter a digit. Rerun program")
             
    def isvalid_weight_final(self):

        if self.weight_final.isdigit():
            self.weight_final = int(self.weight_final)
            if 50 <= self.weight_final <= 80:
                return self.weight_final
            else:
                print("Invalid final weight. (50-80kg) Rerun program")
                return False
        else:
            print("Enter a digit. Rerun program")

