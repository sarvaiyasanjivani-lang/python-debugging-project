try:
    number = int(input("Enter number: "))
    print(500 / number)
except (ValueError, ZeroDivisionError) as error:
    print("Error:", error)
