from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # check if ball hits top or bottom of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()

    # check if ball hits a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_bounce_x()

    # check if right paddle misses
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    # check if left paddle misses
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()










screen.exitonclick()