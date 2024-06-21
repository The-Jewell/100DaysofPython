import random
import turtle as t


#code used to extract colors from image
# import colorgram
#
# rgb_colors= []
# colors = colorgram.extract("img.jpeg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# color list extracted from image
color_list = [(138, 80, 54), (185, 163, 126), (139, 166, 175), (60, 111, 132), (18, 42, 73), (137, 62, 87),
              (163, 153, 44), (66, 118, 100), (147, 182, 171), (214, 209, 110), (76, 34, 29), (70, 151, 163),
              (113, 40, 33), (97, 145, 118), (179, 149, 163), (73, 30, 36), (165, 101, 128), (104, 121, 166),
              (34, 54, 105), (105, 38, 46), (174, 105, 89), (208, 181, 193), (175, 201, 195), (26, 92, 75),
              (10, 94, 108), (160, 202, 209)]

# change color scheme to accept RGB values
t.colormode(255)
# create new turtle object, set speed, shape, color of turtle
turtle = t.Turtle()
turtle.speed("fastest")
turtle.hideturtle()
# moves turtle start point to top left
turtle.teleport(-375, 350)
# picks penup so line isnt drawn as turtle moves
turtle.penup()


number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    # creates new line after 10 dots
    if dot_count % 10 == 0:
        turtle.setheading(270)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)






# creates screen and close event
screen = t.Screen()
screen.exitonclick()







