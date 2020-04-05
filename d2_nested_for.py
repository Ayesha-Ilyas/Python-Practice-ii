my_grid=[
    [1,2,3],
    [2,3,4],
    [5,4,2]
]
print (my_grid[1][2])



x=0
for row in my_grid[x]:
    print(row)
    y = 0
    for col in my_grid[y]:
        print(col)
        y+=1
    x+=1



for horizontal in my_grid:
    print(horizontal)
for horizontal in my_grid:
    for vertical in horizontal:
        print(vertical)


