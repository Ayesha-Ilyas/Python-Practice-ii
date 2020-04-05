try:
    ans = 10 / 0
    print("hey see the magic")
except ZeroDivisionError:  # declare any error which is already in the library
    print("zero error")


try:
    number = int(input("enter a word: "))
except ValueError as any_variable_name:
    print(any_variable_name)
except:
    print("try some specific error")
