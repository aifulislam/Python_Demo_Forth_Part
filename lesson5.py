# 24/12/2020-------
# Tamim Shahriar Subeen-------
# Function()----------------

def add(n1, n2):
    return n1 + n2

n = 10
m = 5

result = add(n, m)
print(result)

n1 = 10
n2 = 10

result = add(n1, n2)
print(result)

num1 = 20
num2 = 10
print(add(num1, num2))

print(add(2.5, 3.9))

# Turtle----------
import turtle
def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

counter = 0

while counter < 90:
    draw_square(100)
    turtle.right(4)
    counter += 1

turtle.exitonclick()

# Function()----------------
def myfnc(x):
    print("inside myfnc", x)
    x = 10
    print("Inside myfnc", x)

x = 20
myfnc(x)
print(x)

# Function()----------------
def myfnc(y):
    print("Y = ", y)
    print("x =", x)

x = 20
myfnc(20)

# Function()----------------
def myfnc(y=10):
    print("y = ", y)


p = 20
myfnc(p)
myfnc()

# Function()----------------
def myfnc(x, y = 10, z = 0):
    print("x =", x, "y =", y, "z =",z)

x = 5
y = 6
z = 7

myfnc(x, y, z)
myfnc(x, y)
myfnc(x)

# Function()----------------
def myfnc(x, z, y = 10):
    print("x =", x, "y =", y, "z =",z)

myfnc(x = 1, y = 2, z = 5)
a = 5
b = 6
myfnc(x = a, z= b)
a = 1
b = 2
c = 3
myfnc(y = a, z = b, x = c)

# Function()----------------
def add_numbers(numbers):
    result = 0

    for number in numbers:
        result += number
    return result

result = add_numbers([1, 2, 30, 4, 5, 9])
print(result)


# Function()----------------
def test_fnc(li):
    li[0] = 10

my_list = [1, 2, 3, 4]
print("before function call", my_list)
test_fnc(my_list)
print("after function call", my_list)


# Function()----------------
list1 = [1, 2, 3, 4]
list2 = list1
print(list1)
list2[0] = 100
print(list2)
print(list1)

# Function()----------------
li = [1, 2, 3]
result = sum(li)
print(result)

# Function()----------------
def add_numbers(numbers):
    result = 0

    for number in numbers:
        result += number / number
    return result

result = add_numbers([1, 2, 30, 4, 5, 7, 4, 9])
print(result)


# ------------End------------- #















