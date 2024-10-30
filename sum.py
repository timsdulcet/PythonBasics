try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sum = num1 + num2
    print("Sum is: ",sum)
except Exception as e:
    print("An error occured",e)
finally:
    print("Report to ADMIN")