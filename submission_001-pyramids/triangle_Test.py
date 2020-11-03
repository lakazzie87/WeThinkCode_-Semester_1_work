height = int(input("Enter the height: "))
x = 0
y = 0
for x in range(0, height):
    for y in range(0, height):
        if y == 0 or x == (height-1) or x == y:
            print("*", end="")
        else:
            print(end=" ")
    print()


    height = 0
    for x in range(1, pyramid+1) # rows
        for y in range(1, pyramid):
            print(' ', end= '')
    
    while(height != (2 * x - 1)):