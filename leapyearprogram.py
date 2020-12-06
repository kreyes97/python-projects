#  Kenneth Reyes
#  This month has __ days in it.

import time

def leapcheck(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 != 0:
        return False
    else:
        return True


def isLeapYear():
    month = int(input("\nEnter a month in numerical form:\n"))
    year = int(input("\nEnter a year in numerical form:\n"))
    monthandday = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December" }
    monthwith31 = [1, 3, 5, 7, 8, 10, 12]
    monthwith30 = [4, 6, 9, 11]

    if month in monthwith31:
        print(f"\n{monthandday[month]} has 31 days in it.\n")
    elif month in monthwith30:
        print(f"\n{monthandday[month]} has 30 days in it.\n")
    elif month != 2:
        print("\nThat is not a month.\n")
    else:
        if leapcheck(year) == True:
            print(f"\n{monthandday[month]} has 29 days in it.\n")
        else:
            print(f"\n{monthandday[month]} has 28 days in it.\n")
    
    cont()

def cont():
    proceed = input("\nWould you like to enter another month and year? Enter Y for yes and N for no.\n").lower()
    while True:
        if proceed == "n":
            print("\nSee you next time!\n")
            time.sleep(1)
            break
        elif proceed != "y":
            print("\nSorry, I didn't quite get that!\n")
            proceed = input("\nWould you like to enter another month and year? Enter Y for yes and N for no.\n").lower()
            continue
        else:
            isLeapYear()
            continue

isLeapYear()