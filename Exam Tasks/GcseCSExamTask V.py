
PERIOD = int(5 * (60 / 5)) # 5 hours times (60 minutes divided by 5 minute readings)
MIN_TEMP = 22
MAX_TEMP = 24
COOLING_REQ = 24.5
HEATING_REQ = 21.5

temperatures = []
out_of_range = []
below_range = []
above_range = []

print("Temperature Measurement and Control Mechanism (Apartment 101)")

def heatReq():

    print(f"Temperature matches heating requirement of {HEATING_REQ} degrees C")
    print("Heating activated")


def coolReq():

    print(f"Temperature matches cooling condition of {COOLING_REQ} degress C")
    print("Cooling activated")


def entryofTemp():

    entries = 0

    for entry in range(PERIOD):
        entries += 1
        print(f"Entry nr: {entries}")

        entry = float(input("Temperature: "))
        temperatures.append(entry)

        if MIN_TEMP <= entry <= MAX_TEMP:
            print("The temperature entry is within the stable range")

        if entry < MIN_TEMP:
            below_range.append(entry)
            out_of_range.append(entry)
            print("The temperature entry is below the stable range")

            if entry == HEATING_REQ:
                heatReq()

        elif entry > MAX_TEMP:
            above_range.append(entry)
            out_of_range.append(entry)
            print("The temperature entry is above the stable range")

            if entry == COOLING_REQ:
                coolReq()

def processTemps():

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    rangeof_temps = max_temp - min_temp
    outofrange_count = len(out_of_range)

    print("----------RESULTS----------")
    print(f"The highest recorded entry for the 5 hour period is {max_temp} degrees C")
    print(f"The lowest recorded temperature for the 5 hour period is {min_temp} degrees C")
    print(f"The difference between the highest and lowest temperature is {rangeof_temps} degress C")
    print(f"The number of times the recorded temperatures were out of the stable range is {outofrange_count}")
    print(f"The temperature was too low {len(below_range)} times and too high {len(above_range)} times")

entryofTemp()
processTemps()






        