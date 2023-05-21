MAX_DIMENSION = 80
MAX_WEIGHT = 10000
MAX_SUMOFDIMENSIONS = 200
MAX_VOLUME = 512000
MIN_PRICE = 10 

def check_volume_length():
    while True:
        length = input("What is the length of the parcel(in cm)? ")
        if length.isdigit():
            length = int(length)
            if 0 < length <= MAX_DIMENSION:
                break
            else:
                print(f"The parcel has been rejected for the length of the parcel should be a non-zero value smaller than or equal to {MAX_DIMENSION}")
        else:
            print("Please enter a digit.")
    return length

check_volume_length()

def check_volume_breadth():
    while True:
        breadth = input("What is the breadth of the parcel (in cm)? ")
        if breadth.isdigit():
            breadth = int(breadth)
            if 0 < breadth <= MAX_DIMENSION:
                break
            else:
                print(f"The parcel has been rejected for the breadth of the parcel should be a non-zero value smaller than or equal to {MAX_DIMENSION}")
        else:
            print("Please enter a digit")
    return breadth

check_volume_breadth()

def check_volume_height():
    while True:
        height = input("What is the height of the parcel(in cm)? ")
        if height.isdigit(): 
            height = int(height)
            if 0 < height <= MAX_DIMENSION:
                break
            else: 
                print(f"The parcel has been rejected for the height of the parcel should be a non-zero value smaller than or equal to {MAX_DIMENSION}")
        else:
            print("Please enter a digit")
    return height

check_volume_height()

def check_weight():
    while True:
        weight = input("How much does the parcel weigh(in grams)? ")
        if weight.isdigit():
            weight = int(weight)
            if 0 < weight <= MAX_WEIGHT:
                break 
            else:
                print(f"The parcel has been rejected for the weight of the parcel should be a non-zero value smaller than or equal to {MAX_WEIGHT}")
        else:
            print("Please enter a digit. ")
    return weight 

check_weight()

def main():
    length = check_volume_length()
    breadth = check_volume_breadth()
    height = check_volume_height()
    weight = check_weight()

    parcel_volume = (length * breadth * height)

    price_per_parcel = ((((weight - 5000) / 100) * .10) + MIN_PRICE)

    while True:
        new_parcel = input("Do you want to add another parcel? (Y for yes and N for no)")
        if new_parcel == "N":
            break
        elif new_parcel == "Y":
            main()
            #hence the main program will rerun for more parcels

    if length + breadth + height <= MAX_SUMOFDIMENSIONS:
        print(f"The parcel of volume {parcel_volume} cm^3 and weight {weight} g has been accepted for delivery. The total cost is ${price_per_parcel}")
    else:
        print(f"The parcel of volume {parcel_volume} cm^3 and weight {weight} g has been rejected as it does not follow the {MAX_SUMOFDIMENSIONS} cm max sum of dimensions policy ")

main()

def checkout():
    #I now want to calculate how many parcels they have registered and the total cost for the package...










#this code does not appear to be correspond with the rest of the program's boundaries:

#parcel_volume = length * breadth * height
#if parcel_volume <= MAX_VOLUME:
        #print(f"Where volume and weight is concerned, the parcel of volume {parcel_volume} cm^3 and weight {weight} kg has been accepted for delivery.")
    #else:
        #print(f"Where volume is concerned, the parcel of volume {parcel_volume} cm^3 and weight {weight} kg has been rejected due to not all dimensions obeying the {MAX_DIMENSION} cm max policy")
