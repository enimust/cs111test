# CS111 Spring 2020
# Extra practice writing functions
# 02/10/20 lecture

def squareDiff(x, y):
    '''Returns the positive difference between the squares of
    the two given numbers'''
    return abs(x*x - y*y)
    

    
def lucky():
    '''Returns a random integer between [1, 100] inclusive'''
    return random.randint(1,100)
    
def lottery():
    '''Prints a triplet of 3 randomly selected numbers'''
    print(lucky(), lucky(), lucky())
    
def greeting():
    '''Prints a friendly personalized greeting after
    asking for the person's name'''
    name = input('Please tell me your name: ')
    print('Hellooooooo '+name+'! So glad to see you!')
    
def splitSquare(size, c1, c2):
    '''Draws a square of size with the left half color c1
    and the right half color c2'''
    pencolor(c1)
    fillcolor(c1)
    # draw the left half of the square, which is a rect
    begin_fill()
    drawRectangle(size/2, size)
    end_fill() 
    leap(size/2)
    pencolor(c2)
    fillcolor(c2)
    # draw the right side of the square
    begin_fill()
    drawRectangle(size/2, size)
    end_fill()