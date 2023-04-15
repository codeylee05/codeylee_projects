
from ExamTaskIII_Pupil import Pupil

CLASSLIST = 30

store_pupils = []

def data_entry():
     pupils = 0

     for pupil in range(CLASSLIST):
          pupils += 1
          print("Pupil nr. ", pupils)

          name = input("Name of pupil: ")
          weight_initial = input("Weight at the beginning of the month: ")
          weight_final = input("Weight at the end of the month: ")

          pupil = Pupil(name, weight_initial, weight_final)

          store_pupils.append(pupil)
          
          return_name = pupil.store_name()
          validate_weight1 = pupil.isvalid_weight_initial()
          validate_weight2 = pupil.isvalid_weight_final()
          '''
          return_data = pupil.store_data() #the data for each pupil object will returned zipped
          
          print(return_data)
          '''
          print(return_name, validate_weight1, validate_weight2)

data_entry()

def return_data():
     for pupil in store_pupils:
          weight_diff = pupil.weight_final - pupil.weight_initial
       
     for pupil in store_pupils:
          print((pupil.name, pupil.weight_initial, pupil.weight_final, "weightdiff:", weight_diff))

return_data()

def calc_weightdiff():
     special_weightdiffs = []

     for pupil in store_pupils:
          weight_diff = pupil.weight_final - pupil.weight_initial
          if weight_diff > 2.5 or -2.5 > weight_diff:
               special_weightdiffs.append((pupil.name, weight_diff))
     

 
     
     print("The following pupils exhibit a weightdiff higher than 2.5kg: ", special_weightdiffs)

calc_weightdiff()
