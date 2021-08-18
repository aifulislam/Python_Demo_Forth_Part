# 24/12/2020-------
# Tamim Shahriar Subeen-------
# Python Data Structure----------------
# Random----------

import turtle
import random

for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x, y)
    turtle.dot()

turtle.done()

# Random----------
import turtle
import random
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x, y)
    turtle.dot()

turtle.done()

# Random----------
import turtle
import random

turtle.penup()

for i in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x, y)
    turtle.dot()

turtle.done()

# Random----------
import turtle
import random
# list of colors
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]

turtle.penup()

for i in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    # set a random position
    turtle.setposition(x, y)
    # set a random color
    i = random.randint(0, len(colors)-1)
    turtle.dot(colors[i])

turtle.done()

# Random----------
import turtle
import random

# list of colors
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]
turtle.penup()
for i in range(50):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    # set a random position
    turtle.setposition(x, y)
    # set random color
    i = random.randint(0, len(colors)-1)
    turtle.dot(colors[i])

turtle.done()


# Find in random------------
import random
number = random.randint(1, 1000)
attempts = 0
while True:
    input_number = input("Guess the number (between 1 and 1000): ")
    input_number = int(input_number)
    attempts += 1
    if input_number == number:
        print("Yes, your guess is correct!")
        break
    if input_number > number:
        print("Incorrect! Please try to guess a smaller number.")
    else:
        print("Incorrect! Please try to guess a smaller number.")

print("You tried", attempts, "times to find the correct number.")

# Find in random------------
import random
number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000

while True:
    print("Guess the number (between 1 and 1000): ")
    input_number = (low + high) // 2
    print("My guess is", input_number)
    attempts += 1
    if input_number == number:
        print("Yes, your guess is correct!")
        break
    if input_number > number:
        print("Incorrect! Please try to guess a smaller number.")
        high = input_number - 1
    else:
        print("Incorrect! Please try to guess a smaller number.")
        low = input_number + 1


print("You tried", attempts, "times to find the correct number.")


# Turtle---------
import turtle
turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        break

turtle.end_fill()
turtle.done()

# Turtle------------
import turtle
turtle.color('red', 'orange')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        break


turtle.end_fill()
turtle.done()

# Turtle-------------
import turtle
turtle.begin_fill()
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.end_fill()

# Turtle-------------
import turtle
r = 120
a = 180
turtle.circle(r, a)
turtle.done()

# ----------End-------#
