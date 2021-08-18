#22/12/2020-------
#Tamim Shahriar Subeen-------
#Conditional Logic-----

a = 2
b = 3
print(a == b)

a = 3
b = 3
print(a == b)

a = 2
b = 3
print(a != b)

a = 2
b = 3
print(a > b)

a = 2
b = 3
print(a < b)

a = 2
b = 3
print(a >= b)

a = 2
b = 3
print(a <= b)

a = "Bangladesh"
b = "Bangladesh"
print(a == b)

a = "Bangladesh"
b = "bangladesh"
print(a == b)

my_money = 30
rickshaw_fare = 40
if my_money >= rickshaw_fare:
    print("True")
else:
    print("False")


my_money = 30
rickshaw_fare = 30
if my_money >= rickshaw_fare:
    print("True")
else:
    print("False")


my_money = 50
rickshaw_fare = 40
if my_money >= rickshaw_fare:
    print("True")
else:
    print("False")


today = "Tuesday"
if not today == "Tuesday":
    print("True")
else:
    print("False")

n1 = 20
if n1 > 10:
    print("Yes")
else:
    print("No")

n1 = 20
if n1 < 10:
    print("Yes")
else:
    print("No")


n1 = 20
if n1 > 10 and n1 < 100:
    print("Yes")
else:
    print("No")


n1 = 20
if n1 == 10:
    print("Yes")
else:
    print("No")


n1 = 20
if n1 != 10:
    print("Yes")
else:
    print("No")

n1 = 20
if n1 > 10 or n1 < 100:
    print("Yes")
else:
    print("No")


n1 = 200
if not n1 > 300 or n1 < 100:
    print("Yes")
else:
    print("No")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(numbers))
print(numbers[0])

saarc = ["Bangladesh", "Pakistan", "India", "Afghanistan", "Bhutan", "Nepal", "Sri lanka"]
print(saarc)
print("Number of countries in SAARC: ", len(saarc))
print(saarc[0])
print(saarc[6])

#True of False------
if "Bangladesh" in saarc:
    print("Yes")
else:
    print("No")

#True of False------
if "China" in saarc:
    print("Yes")
else:
    print("No")

#True of False------
if "Bangladesh" not in saarc:
    print("Yes")
else:
    print("No")


#True of False------
if "China" not in saarc:
    print("Yes")
else:
    print("No")


#if statmment----
saarc = ["Bangladesh", "Pakistan", "India", "Afghanistan", "Bhutan", "Nepal", "Sri lanka"]

country = input("Enter the name of the country: ")
if country in saarc:
    print(country, "is a member of SAARC")

print("Program terminated")

#if statmment----
saarc = ["Bangladesh", "Pakistan", "India", "Afghanistan", "Bhutan", "Nepal", "Sri lanka"]

country = input("Enter the name of the country: ")
if country in saarc:
    print(country, "is a member of SAARC")
else:
    print(country, "is not a member of SAARC")

print("Program terminated")

#Grade------
marks = input("Please enter your marks: ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"

print("Your grade is", grade)


# Positive or  Negative-------
number = input("Enter a intiger number: ")
number = int(number)
if number >= 0:
    print("This number is a positive")
else:
    print("This number is a negative")

print("Program terminated")


# Even or  Odd-------
number = input("Enter a intiger number: ")
number = int(number)
if number %2 == 0:
    print("This number is Even")
else:
    print("This number is Odd")

print("Program terminated")

# Find in Maximum or Minimum nubmber----

n1 = 40
n2 = 60
n3 = 30

if n1 > n2:
    max_n = n1
else:
    max_n = n2
if n3 > max_n:
    max_n = n3

print("Maximum: ", max_n)

# Find in Maximum or Minimum nubmber----

n1 = 40
n2 = 60
n3 = 30

if n1 < n2:
    min_n = n1
else:
    min_n = n2
if n3 < min_n:
    min_n = n3

print("Minimum: ", min_n)

# Input Three numbers then find a maximum number----
n1 = input("Enter a First number: ")
n1 = int(n1)
n2 = input("Enter a Second number: ")
n2 = int(n2)
n3 = input("Enter a Third number: ")
n3 = int(n3)

if n1 > n2:
    max_n = n1
else:
    max_n = n2
if n3 > max_n:
    max_n = n3

print("Maximum", max_n)


# Input Three numbers then find a Minimum number----
n1 = input("Enter a First number: ")
n1 = int(n1)
n2 = input("Enter a Second number: ")
n2 = int(n2)
n3 = input("Enter a Third number: ")
n3 = int(n3)

if n1 < n2:
    min_n = n1
else:
    min_n = n2
if n3 < min_n:
    min_n = n3

print("Minimum", min_n)

# Leap Year-------


# Leap Year----------
year = input("Enter your year: ")
year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")


# Leap Year----------
if year % 4 != 0:
    print("No")
else:
    if year % 100 != 0:
        print("Yes")
    else:
        if year % 400 != 0:
            print("No")
        else:
            print("Yes")


# Leap Year----------
year = input("Enter your year: ")
year = int(year)
if year % 400 == 0:
    print("Yes")
elif year % 100 == 0:
    print("No")
elif year % 4 == 0:
    print("Yes")
else:
    print("No")


# Leap Year----------
year = input("Enter your year: ")
year = int(year)
if year % 100 != 0 and year % 4 == 0:
    print(year, "is leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(year, "is leap year")
else:
    print(year, "is not leap year")


