try:
    numerator = int(input("enter no to div"))
    denominator = int(input("enter the no to div by"))
    result = numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You cant div by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print("Something went wrong")

finally:
    print("Done!")
