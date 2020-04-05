def ex_fun(b_n, p_n):
    result = 1
    for index in range(p_n):
        result = result * b_n
    return result


b_n = input("Enter an integer num: ")
p_n = input('Enter an integer num: ')
print(ex_fun(int(b_n),int(p_n)))
