

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower()
    if shape == "triangle" or shape == "square" or shape == "pyramid" or shape == "rectangle" or shape == "rhombus": 
        #print(shape)
        return shape
    else:
        return get_shape()

# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = ''
    while height.isnumeric() != True:
        height = input("Height?: ")
    height = int(height)
    return height 

# TODO: Step 2"""
def draw_pyramid(height, outline):
    space =  height - 1
    stars = 1
    if outline is True:
        j = 1
        height -= 2
        h = height #actually the height
        print(" "*(height+1)+ "*")
        while 0 < (height):
            print(" " * (height) + "*" + " " * j + "*")
            j += 2 #space counter
            height -= 1 #controls the 'x'        
            if height == 0:
                print("*" * (h * 2 + 3))
        
    else:
        for x in range(height):
            print(" " * space + "*" * stars)
            space = space - 1
            stars = stars + 2
        #print()
            #print(draw_pyramid)

# TODO: Step 3
def draw_square(height, outline):
    if outline is True:
        i = 0
        print("*" * height)
        while i < (height - 2):
            print("*" + " " * (height - 2) + "*")
            i += 1
        print("*" * height)
    
    else:
        
        for x in range(0, height):
            for y in range(0, height):
                print("*", end= '')
            print()

        """        
        #print(draw_square)
        for x in range(height):
            print("*" * height)    
        """

def draw_rectangle(height, outline):
    if outline is True:
        i in range(1, height + 1):
        for 

        i = 0
        print("*" * height)
        while i < (height - 2):
            print("*" + " " * (height - 2) + "*")
            i += 1
        print("*" * height)
    
    else:
       for row in range(0, height):
            print("*" * height)

    """

def draw_rhombus(height, outline):
    if outline is True:	
		space =  height - 1
        stars = 1
        j = 1
        height -= 2
        h = height #actually the height
        print(" "*(height +1)+ "*")
        while 0 < (height):



    else:
       
"""

# TODO: Step 4
def draw_triangle(height, outline):
    if outline is True:
        print("*")
        print("**")
        i = 3
        j = 1
        while i < height:
            print("*" + (" " * j) + "*")
            i += 1
            j += 1
        print("*" * height, end= '')
        print()  
    else:
        for x in range(0,(height)):
            for y in range(0, x + 1):
                print("*", end= '')
            print()

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'rectangle':
        draw_rectangle(height, outline)
    elif shape == 'rhombus':
        draw_rhombus(height, outline)



# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (Y/N)").lower()
    if outline == "n":
        return False
    else:
        return True       



if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

