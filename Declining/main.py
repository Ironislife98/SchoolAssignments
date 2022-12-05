def Declining():
    print("Attendance has been steadily declining at weekly religious services from 1985.")
    print("This program displays the percentage of the Canadian population that attends a weekly religious service for any year from 1985 to 2025.\n")
    percentages = []
    for year in range(41):
        percentages.append(30 - (year * .45))
    while True:
        year = int(input("Please select a year: "))
        print()
        print(f"The percentage of weekly attendance for {year} is {percentages[year - 1985]}%\n")
        tryagain = input("Enter 1 to select another year, or any other value to exit:")
        if tryagain != "1":
            break
        print()
Declining()