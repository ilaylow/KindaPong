import turtle
import os
import time
import random

window = turtle.Screen()
window.title("Pong Trial")
window.bgcolor("black")
window.setup(width=600, height=600)

window.tracer(0)

delay = 0.02

# Title

title = turtle.Turtle()
title.speed()
title.shape("square")
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 260)
title.write("PONG", align="center", font=("Arial", 25, "normal"))

#Player 1 Construction 

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(3,0.2,1)
player1.color("white")
player1.penup()
player1.goto(-225,0)
player1.direction = "stop"

#Player 2 Construction 

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(3,0.2,1)
player2.color("white")
player2.penup()
player2.goto(225,0)
player2.direction = "stop"

#Ball Construction

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.direction = "up_up_right"

# Scores

score = turtle.Turtle()
score.speed()
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(-150, 260)
score.write("Score: 0", align="center", font=("Arial", 15, "normal"))

score2 = turtle.Turtle()
score2.speed()
score2.shape("square")
score2.color("white")
score2.penup()
score2.hideturtle()
score2.goto(150, 260)
score2.write("Score: 0", align="center", font=("Arial", 15, "normal"))

# Winning Title

win = turtle.Turtle()
win.shape("square")
win.color("white")
win.penup()
win.hideturtle()
win.goto(0, -200)


#Functions 

def go_up():
    
    if player1.ycor() <= 250:
        player1.sety(player1.ycor() + 40)

def go_down(): 

    if player1.ycor() >= -250:
        player1.sety(player1.ycor() - 40)

def go_up_2():

    if player2.ycor() <= 250:
        player2.sety(player2.ycor() + 40)

def go_down_2():

    if player2.ycor() >= -250:
        player2.sety(player2.ycor() - 40)

speed = 4.5

def move_ball():
    x = ball.xcor()
    y = ball.ycor()

    ### ADD MORE DIRECTIONS

    if ball.direction == 'up_up_right':
        ball.setx(x + speed - 2)
        ball.sety(y + speed + 2)

    if ball.direction == 'down_down_right':
        ball.setx(x + speed - 2)
        ball.sety(y - speed - 2)

    if ball.direction == 'up_up_left':
        ball.setx(x - speed + 2)
        ball.sety(y + speed + 2)
    
    if ball.direction == 'down_down_left':
        ball.setx(x - speed + 2)
        ball.sety(y - speed - 2)

    if ball.direction == 'up_right':
        ball.setx(x + speed)
        ball.sety(y + speed)
    
    if ball.direction == 'up_left':
        ball.setx(x - speed)
        ball.sety(y + speed)

    if ball.direction == 'down_right':
        ball.setx(x + speed)
        ball.sety(y - speed)   

    if ball.direction == 'down_left':
        ball.setx(x - speed)
        ball.sety(y - speed)


window.listen()

window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")

window.onkeypress(go_up_2, "Up")
window.onkeypress(go_down_2, "Down")

# Initial value score

p1score = 0
p2score = 0

while True:
    window.update()

    player1_ball_x = abs(player1.xcor() - ball.xcor())

    player2_ball_x = abs(player2.xcor() - ball.xcor())

    player1_ball_y = ball.ycor() - player1.ycor()

    player2_ball_y = ball.ycor() - player2.ycor()

    # Rebound for Ball

    if ball.ycor() > 280 and ball.direction == "up_right":
        ball.direction = "down_right"

    elif ball.ycor() > 280 and ball.direction == "up_left":
        ball.direction = "down_left"
    
    elif ball.ycor() < -280 and ball.direction == "down_right":
        ball.direction = "up_right"

    elif ball.ycor() < -280 and ball.direction == "down_left":
        ball.direction = "up_left"
    
    elif ball.ycor() > 280 and ball.direction == "up_up_right":
        ball.direction = "down_down_right"

    elif ball.ycor() > 280 and ball.direction == "up_up_left":
        ball.direction = "down_down_left"
    
    elif ball.ycor() < -280 and ball.direction == "down_down_right":
        ball.direction = "up_up_right"
    
    elif ball.ycor() < -280 and ball.direction == "down_down_left":
        ball.direction = "up_up_left"

    # Ball - Player Collision

    if player1_ball_x < 20 and player1_ball_x > 0 and player1_ball_y > 20 and player1_ball_y < 40:
        ball.direction = "up_up_right"
        speed += 0.5

    if player1_ball_x < 20 and player1_ball_x > 0 and player1_ball_y > 0 and player1_ball_y < 20:
        ball.direction = "up_right"
        speed += 0.5

    if player1_ball_x < 20 and player1_ball_x > 0 and player1_ball_y < 0 and player1_ball_y > -20:
        ball.direction = "down_right"
        speed += 0.5

    if player1_ball_x < 20 and player1_ball_x > 0 and player1_ball_y < -20 and player1_ball_y > -40:
        ball.direction = "down_down_right"
        speed += 0.5

    if player2_ball_x < 20 and player2_ball_x > 0 and player2_ball_y > 0 and player2_ball_y < 20:
        ball.direction = "up_left"
        speed += 0.5
    
    if player2_ball_x < 20 and player2_ball_x > 0 and player2_ball_y > 20 and player2_ball_y < 40:
        ball.direction = "up_up_left"
        speed += 0.5

    if player2_ball_x < 20 and player2_ball_x > 0 and player2_ball_y < 0 and player2_ball_y > -20:
        ball.direction = "down_left"
        speed += 0.5

    if player2_ball_x < 20 and player2_ball_x > 0 and player2_ball_y < -20 and player2_ball_y > -40:
        ball.direction = "down_down_left"
        speed += 0.5    
    
    # Scoring
    
    if ball.xcor() > 280:
        p1score += 1
        score.clear()
        score.write("Score: {}".format(p1score), align="center", font=("Arial", 15, "normal"))
        ball.goto(0,0)  
        speed = 5

    if ball.xcor() < -300:
        p2score += 1
        score2.clear()
        score2.write("Score: {}".format(p2score), align="center", font=("Arial", 15, "normal"))
        ball.goto(0,0)
        speed = 5

    if p2score == 11:
        win.write("Player 2 Wins!", align="center", font=("Arial", 15, "normal"))
        break

    elif p1score == 11:
        win.write("Player 1 Wins!", align="center", font=("Arial", 15, "normal"))
        break

    move_ball()

    time.sleep(delay)

window.mainloop()



