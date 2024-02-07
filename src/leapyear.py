year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap")
        else:
            print("It is not a leap")

    else:
        print("It is a leap")
else:
    print("It is not a leap")

    