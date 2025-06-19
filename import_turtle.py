# import turtle
#
# # turtle.pendown()
# # turtle.forward(100)
# # turtle.right(90)
# # turtle.forward(100)
# # turtle.right(90)
# # turtle.done()

import turtle
from math import radians, cos


def square(length: int) -> None:
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)


def encircled_square(length: int) -> None:
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    turtle.left(135)
    print(f'Inside function, namespace is: {dir()}')
    print(f'Locals: {locals()}')


# encircled_square(300)
# turtle.speed(0)
# for s in range(72):
#     encircled_square(120)
#     turtle.left(5)
# turtle.done()

print(dir())
g = globals()
print(g['square'])
print(dir(__builtins__))