def TemperatureStats():
    print("This program records the daily maximum temperatures for a week, and then outputs the average weekly high temperature.")
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    temps = []
    for day in days:
        temps.append(float(input(f"Please enter the temperature for {day}: ")))
    print()
    for day in range(len(days)):
        print(f"Your daily high temperature for {days[day]} is {temps[day]}")
    print()
    average = 0
    for temp in temps:
        average += temp
    average /= len(temps)
    print(f"The average weekly high temperature is: {round(average, 1)}")
TemperatureStats()