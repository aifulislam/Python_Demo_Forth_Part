

# Prime number 1-----------
def is_prime1(n):
    if n < 2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divisible by", x)
            prime = False
        return prime
while True:
    number = input("Please enter a number (enter 0 to exit): ")
    number = int(number)
    if number == 0:
        break
    prime = is_prime1(number)
    if prime is True:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

# Prime number 2----------
def is_prime2(n):
    if n < 2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divisible be", x)
            prime = False
            return prime
    return prime

while True:
    number = input("Please enter a number (enter 0 to exit): ")
    number = int(number)

    if number == 0:
        break

    prime = is_prime2(number)
    if prime is True:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

# Prime number 3--------------
def is_prime3(n):
    if n == 2:
        return True
    if n % 2 == 0:
        print(n, "is divisible by 2")
        return False
    if n < 2:
        return False
    prime = True
    for x in range(3, n, 2):
        if n % x == 0:
            print(n, "is divisible by", x)
            prime = False
            return prime
    return prime

# Prime number 4------------
import math

def is_prime4(n = 1013):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int()
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True

# Fibonacci Number------------
fib_x = 1
fib_next = 1
n = input()
n = int()
if n <= 2:
    fib_n = 1
else:
    i = 3
    while i <= n:
        i += 1
        fib_temp = fib_x + fib_next
        fib_x = fib_next
        fib_next = fib_temp
    fib_n = fib_next
print(fib_n)

# Fibonacci Number------------
fib_x = 1
fib_next = 1
n = input()
n = int()
if n <= 2:
    fib_n = 1
else:
    i = 3
    while i <= n:
        i += 1
        fib_next, fib_x = fib_next + fib_x, fib_next

    fib_n = fib_next
print(fib_n)
