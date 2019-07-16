import turtle


'''README
-run with python 3

- control with arrow keys, forward = move forward 5cm, backward = vice

- p to toggle line drawing (for repositioning roomba)

- , and . trim the virtual roomba by 10 degrees

- s to place a stamp of the virtual roomba, intented to track where the roomba
found a ledge

- to add an obstacle, press c, then enter in the console
"distance angle diameter" without the quotations, ex:23 120 30.5.
I recommend you try this out because its pretty neat.
 '''

roomba = turtle.Turtle() #get the screen & turtle
screen = turtle.Screen()

screen.setup(427 * 2, 244 * 2) #Screen setup
screen.title('Dancing Roomba')
screen.bgcolor("purple")
roomba.color("cyan")

typing = False

def left(): #Virtual Roomba functions
    if(typing == False):
        roomba.left(90)

def right():
    if(typing == False):
        roomba.right(90)

def forward():
    if(typing == False):
        roomba.forward(10)

def backward():
    if(typing == False):
        roomba.back(10)

def pen():
    if(typing == False):
        if(roomba.isdown()):
            roomba.penup()
        else:
            roomba.pendown()

def trimLeft():
    if(typing == False):
        roomba.left(10)

def trimRight():
    if(typing == False):
        roomba.right(10)

def command():
    global typing #enable editing for typing
    typing = True

    com = input()
    print('You entered', com)

    arr = com.split( ) #get the command and current roomba values
    pos = roomba.pos()
    angle = roomba.heading()

    roomba.penup()  #draw the circle
    roomba.seth(angle - 90 + float(arr[1]))
    roomba.forward(float(arr[0]) * 2)
    roomba.pendown()
    roomba.circle(float(arr[2]))
    roomba.penup()

    roomba.setpos(pos) #return roomba to original position
    roomba.seth(angle)
    roomba.pendown()
    typing = False

def stamp():
    roomba.stamp()



screen.onkey(left, "Left") #Keybindings
screen.onkey(right, "Right")
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(pen, "p")
screen.onkey(trimLeft, 'comma')
screen.onkey(trimRight, 'period')
screen.onkey(stamp, 's')
screen.onkey(command, 'c')

screen.listen() #loop & listen
screen.mainloop()
