# Simple project of Pong game using Python 3.8.
# By @Iampiku
# We will be using Turtle class module in this project.

import turtle 

gm_window = turtle.Screen()                     # this class defines a graphic window.
gm_window.title("PONG")                         # Setting the title name of the window.
gm_window.bgcolor("gray")                      # Setting the background color
gm_window.setup(width = 800, height = 600)      # units of the dimensions are in px
gm_window.tracer(0) 

# We are setting the up out paddle and ball on the game window

# Paddle A
padd_a = turtle.Turtle()
padd_a.speed(0)
padd_a.shape("square")                # adjusting the size and shape of the paddles and the ball
padd_a.shapesize(stretch_wid = 6, stretch_len = 0.5)
padd_a.color("white")
padd_a.penup()                        # this insures that no line is drawn during the movement of the paddle
padd_a.goto(-350, 0)                  # Setting the position of the paddle on the screen

# Paddle B
padd_b = turtle.Turtle()
padd_b.speed(0)
padd_b.shape("square")
padd_b.shapesize(stretch_wid = 6, stretch_len = 0.5)
padd_b.color("white")
padd_b.penup()
padd_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.03                                     # movement of the ball by 2px
ball.dy = 0.03                                     # the movement of the ball will be diagonal as x & y are positive coordinates


# defining a fuctions for the movement of the paddles and the ball

def padd_a_up():

    """ This fuction will move th padd_a to upward direction ( by 20px ) """

    y_coordinate = padd_a.ycor()
    y_coordinate += 20
    padd_a.sety(y_coordinate)

# Keyboard Binding
gm_window.listen()                              # To take input from I/O
gm_window.onkeypress(padd_a_up, "w")            # On pressing 8 from the numpad padd_a_up fuction will be called    

def padd_a_down():

    """ This fuction will move th padd_a to downward direction ( by 20px ) """

    y_coordinate = padd_a.ycor()
    y_coordinate -= 20
    padd_a.sety(y_coordinate)

# Keyboard Binding
gm_window.listen()                              
gm_window.onkeypress(padd_a_down, "s") 

def padd_b_up():
    
    """ This fuction will move th padd_b to upward direction ( by 20px ) """

    y_coordinate = padd_b.ycor()
    y_coordinate += 20
    padd_b.sety(y_coordinate)

# Keyboard Binding
gm_window.listen()                             
gm_window.onkeypress(padd_b_up, "o")            

def padd_b_down():

    """ This fuction will move th padd_b to downward direction ( by 20px ) """

    y_coordinate = padd_b.ycor()
    y_coordinate -= 20
    padd_b.sety(y_coordinate)

# Keyboard Binding
gm_window.listen()                              
gm_window.onkeypress(padd_b_down, "l")


# Game Loop  
while(True):
    gm_window.update()                          # this will update the screen every time the loop runs

    # Movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Top Border Bouncing
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1

    # Bottom Border Bouncing
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1 

    # Left and Right Bouncing
    if (ball.xcor() > 350):
        ball.goto(0,0)
        ball.dx *= -1 
    
    if (ball.xcor() < -350):
        ball.goto(0,0)
        ball.dy *= -1 

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < padd_a.ycor() + 50 and ball.ycor() > padd_a.ycor() - 50:
        ball.dx *= -1 

    elif ball.xcor() > 340 and ball.ycor() < padd_b.ycor() + 50 and ball.ycor() > padd_b.ycor() - 50:
        ball.dx *= -1