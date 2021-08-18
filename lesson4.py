# 24/12/2020-------
# Tamim Shahriar Subeen-------
# Loop()----------------

for i in range(5):
    print("I want to be a good programmer.")


for i in range(5):
    print(i)

import turtle
turtle.shape("turtle")
turtle.speed(5)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.exitonclick()

result = 0
for _ in range(50):
    result = result + 1

print(result)

# Loop----
result = 0
num = 1
for _ in range(50):
    result = result + num
    num = num + 1
    # num += 1

print(result)

# Loop----
result = 0
for num in range(51):
    result = result + num
    # result += num

print(result)

# Loop-----
result = 0
for num in range(1, 51):
    result += num

print(result)


for i in range(1, 20, 5):
    print(i)

# Maximum number---------
numbers = [6, 1, 3, 0, 9, 3, 2, 5]
max_n = numbers[0]

for n in numbers:
    if n > max_n:
        max_n = n

print(max_n)

# Minimum number----------
numbers = [6, 1, 3, 6, 9, 3, 2, 5]
min_n = numbers[0]
for n in numbers:
    if n < min_n:
        min_n = n

print(min_n)


# Loop---------
result = 0
for num in range(101):
    if num % 5 == 0:
        print(num)
        result += num

print("Sum is: ", result)

# Loop------
result = 0
for num in range(5, 101, 5):
    print(num)
    result += num

print("Sum is: ", result)

# Turtle------------
import turtle

turtle.speed(1)

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()
    turtle.pencolor("red")


turtle.exitonclick()

# Nested Loop----------
import turtle
turtle.shape("turtle")
turtle.speed(5)

for l in range(50, 100, 10):
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)

turtle.exitonclick()

saarc = ["Bangladesh", "India", "Afganistan", "Bhutan", "Pakistan", "Nepal", "Sri Lanka"]
for country in saarc:
    print(country, "is a member of SAARC")

li = list(range(11))
print(li)

li = list(range(2, 21, 2))
print(li)

saarc = ["Bangladesh", "India", "Afganistan", "Bhutan", "Pakistan", "Nepal", "Sri Lanka"]
for country in saarc:
    print(country, "is a member of SAARC")

# while loop---------
i = 0
while i < 5:
    print(i)
    i += 1

# while loop---------
i = 5
while i >= 0:
    i -= 1
    print(i)

# Multiplication_table-------
n = input("Please enter a positive integer: ")
n = int(n)

m = 1
while m <= 10:
    print(n, "*", m, "=", n * m)
    m += 1

# Multiplication_table--------
n = input("Please enter a positive number: ")
n = int(n)
m = 1
while m <= 10:
    print(n, "X", m, "=", n * m)
    m += 1




import turtle

turtle.color("red")
turtle.speed(5)
counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1

turtle.exitonclick()


# Turtle-----------
import turtle
height = 5
width = 5

turtle.speed(2)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20 * width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()


# Using break and continue------

while True:
    n = input("Please enter a number (0 to exit): ")
    n = int(n)
    if n == 0:
        break
    print("Square of", n, "is", n * n)
print("0 is unable number")

# Using break and continue------
while True:
    n = input("Please enter a positive number (0 to exit): ")
    n = int(n)
    if n < 0:
        print("We only allow positive number. Please try again. ")
        continue
    if n == 0:
        break
    print("Square of", n, "is", n * n)

# Using break and continue------
terminate = False
while not terminate:
    n1 = input("Please enter a number: ")
    n1 = int(n1)
    n2 = input("Please enter a another number: ")
    n2 = int(n2)

    while True:
        operation = input("Please enter add/sub/mul/div or quit to exit: ")
        if operation == "quit":
            terminate = True
            break
        if operation not in ["add", "sub", "mul", "div"]:
            print("Unknown operation!")
            continue
        if operation == "add":
            print("Result is", n1 + n2)
            break
        if operation == "sub":
            print("Result is", n1 - n2)
            break
        if operation == "mul":
            print("Result is", n1 * n2)
            break
        if operation == "div":
            print("Result is", n1 / n2)
            break


print("The end")

# ------------End------------- #
