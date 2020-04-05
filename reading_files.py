my_file=open("olla world.txt","r")
print(my_file.readable())
my_file.close()
my_file=open("olla world.txt","a")
print(my_file.write('\n kerri>ketra'))
my_file.close()
my_file=open("olla world.txt","r")
print(my_file.readline()[0])
my_file.close()
my_file=open("olla world.txt","r")
print(my_file.readline())
my_file.close()
my_file=open("olla world.txt","r")
print(my_file.readlines())
my_file.close()
my_file=open("olla world.txt","r")
print(my_file.readlines())
my_file.close()
my_file=open("olla world.txt","r")
print(my_file.readlines())
my_file.close()
my_file=open("olla world.txt","r")
print(my_file.readlines())
my_file.close()
my_file=open("olla world.txt","r")
print(my_file.readlines())
my_file.close()


my_file=open("olla world 1.txt","w")
print(my_file.write("\n nenenennenennene,eeeeeeeeeeee"))
my_file.close()

my_file=open("olla world 2.html","w")
print(my_file.write("<p> hello kerry berry carry </p>"))
my_file.close()




my_file=open("olla world.txt","r")
for file in my_file.raedlines():
    print(file)
my_file.close()
