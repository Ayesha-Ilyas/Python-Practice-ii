num= [ 1,2,3,4,5]
alpha= ["are","we" ,"ok" ,"skipped"]
alpha.extend(num)
alpha.pop()
alpha.count("are")
print(alpha.index("are"))
print ("hi"+ str(alpha)+ "skipped"+str(num ))
alpha.extend(alpha)
alpha.remove("are")
alpha.reverse()
alpha.clear()
alpha.sort()
print("hi"+ str(alpha)+ "skipped"+str(num ))
coordinate=[(1,2,3,3,4), (3,4,5,6,), (45,6,7,7)]
coordinate[1]=(2,4556,78,3)
print(coordinate[1])


def ex_fun(b_n, p_n):
    result = 1
    for index in range(p_n):
        result = result * b_n
    return result


b_n = input("Enter an integer num: ")
p_n = input('Enter an integer num: ')
print(ex_fun(int(b_n),int(p_n)))
