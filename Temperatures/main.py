def Temperatures():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    temps = []
    for day in days:
        temps.append(input(f"Please enter the temperature for {day}: "))
    print()
    for day in range(len(days)):
        print(f"Your daily high temperature for {days[day]} is {float(temps[day])}")

Temperatures()