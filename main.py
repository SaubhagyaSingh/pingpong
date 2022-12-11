import turtle
import winsound
window = turtle.Screen()
window.title("Pingpong by saubhi")  # title
window.bgcolor("green")  # screen color
window.setup(width=1280, height=800)  # screen size
window.tracer(0)  # stops auto updating the screen
# score
score_a = 0
score_b = 0

# paddle a
paddle_a = turtle.Turtle()  # module and class
paddle_a.speed(0)  # max speed set
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # stops drawing on screen as turtle in general draws lines on screen
paddle_a.goto(-600, 0)


# paddle b
paddle_b = turtle.Turtle()  # module and class
paddle_b.speed(0)  # max speed set
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # stops drawing on screen as turtle in general draws lines on screen
paddle_b.goto(600, 0)  # sets the position with center as 0,0

# ball
ball = turtle.Turtle()  # module and class
ball.speed(0)  # max speed set
ball.shape("circle")
ball.color("white")
ball.penup()  # stops drawing on screen as turtle in general draws lines on screen
ball.goto(0, 0)
ball.dx = 0.75  # movement of ball by 2 pixels
ball.dy = -0.75

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player A: 0 Player B: 0", align="center",
          font=("Courier", 24, "normal"))
# Movement function


def paddle_a_up():
    y = paddle_a.ycor()  # stores the y coordinates of the object paddle_a in variable y
    y += 20  # adds 20 pixels in y
    paddle_a.sety(y)  # sets the position of object paddle_a with respect to y


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding

window.listen()  # listen for keyboard input
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
# main game loop
while True:
    window.update()
    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
# border checking
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1  # reverses the direction of the ball
    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
    if ball.xcor() > 630:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound('boing.wav', winsound.SND_ASYNC)
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
    if ball.xcor() < -630:
        ball.goto(0, 0)
        ball.dx *= -1
        # dosent works for some reason
        winsound.PlaySound('boing.wav', winsound.SND_ASYNC)
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

# paddle and ball collsion
    if (ball.xcor() > 590 and ball.ycor() < 590) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(590)
        ball.dx *= -1

    if (ball.xcor() < -590 and ball.ycor() > - 590) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-590)
        ball.dx *= -1
