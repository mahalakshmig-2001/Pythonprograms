try:
   #value = 10/0
    number = int(input("Enter number:"))

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid Input")