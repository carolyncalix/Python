x = input("what length do you want as your 1st side?")
y = input("what length do you want at your 2nd side?")
z = input("what length do you want as your 3rd side?")

def triangle(x,y,z):
    if x != y and y != z and x != z:
        print ("scalene triangle")
    else:
        print ("this is not a scalene triangle")
triangle(x,y,z)
