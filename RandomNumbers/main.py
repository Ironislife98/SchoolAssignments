import random

def RandomNumbers(test=False):
    print("Random Number Generator")
    print("=======================")
    print()
    while True:
        sum_nums = 0
        num_random = int(input("Enter the number of random numbers to generate: "))
        lower_range = 0
        upper_range = 0
        while lower_range >= upper_range:
            lower_range = int(input("Enter the lower range: "))
            upper_range = int(input("Enter the upper range: "))
            if lower_range >= upper_range:
                print("Invalid Range")
        randNums = []
        print("GENERATED NUMBERS")
        print("=================")
        if not test:
            for i in range(num_random):
                randNums.append(random.randint(lower_range, upper_range))
                print(randNums[i])
                sum_nums = sum_nums + randNums[i]
            avg_num = 0
            for i in randNums:
                avg_num += i
            avg_num /= len(randNums)
        else:
            testList = []
            testLength = int(input("Number of elements in the test list:"))
            for j in range(testLength):
                testList.append(int(input("")))
            print()
            for i in testList:
                print(i)
                sum_nums += i
                num_random = testLength
            avg_num = 0
            for i in testList:
                avg_num += i
            avg_num /= len(testList)
        print(f"\nAverage of random numbers is: {round(avg_num, 1)}\n")
        if input("Enter 1 to try again, or any other integer to exit: ") != "1":
            break
        print()
RandomNumbers(True)