DAYS_IN_MONTH = 30

#task 1 #data entry and appension to data list, including validation[digit entry]
midday_temps = []
midnight_temps = []
monthly_temps = [] 

month = input("Month? ")

def data_entry():

    for days in range(DAYS_IN_MONTH):
        print(days + 1)

        while True:
            midday_temp = input("What is the midday temperature? ")
            if midday_temp.isdigit():
                midday_temp = int(midday_temp)
                midday_temps.append(midday_temp)
                break
            else:
                print("Value Error(Please enter a digit")
                continue

        while True:
            midnight_temp = input("What is the midnight temperature? ")
            if midnight_temp.isdigit():
                midnight_temp = int(midnight_temp)
                midnight_temps.append(midnight_temp)
                break
            else:
                print("Value Error(Please enter a digit")
                continue

data_entry()

##task 2 #average midday and average midnight
sum_middaytemps = 0
sum_midnightemps = 0

for element in midday_temps:
    sum_middaytemps += element #or: += int(element) assuming the elements were not integers
for element in midnight_temps:
    sum_midnightemps += element #or += int(element) assuming elements were not integers

average_middaytemps = sum_middaytemps / DAYS_IN_MONTH
average_midnighttemps = sum_midnightemps / DAYS_IN_MONTH

#task 3 #highest midday, lowest midnight
max_middaytemp = max(midday_temps)
min_midnighttemp = min(midnight_temps)

#outputs
def result():
    print(f"The average midday temperature for", month, f"is {average_middaytemps} degrees C")
    print(f"the average midnight temperature for", month, f"is {average_midnighttemps}")
    print(f"The highest midday temperature is recorded as", max_middaytemp, f"degrees C on day {midday_temps.index(max_middaytemp) + 1} of", month)
    print(f"The lowest midnight temperature is recorded as", min_midnighttemp, f"degrees C on day {midnight_temps.index(min_midnighttemp) + 1} of", month)

result()






