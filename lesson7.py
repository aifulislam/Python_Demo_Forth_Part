# 24/12/2020-------
# Tamim Shahriar Subeen-------
# Python Data Structure----------------
# List[]----------

# append()-----
# List is Mutable---
we = ["Arif", "Ayon", "Nazim", "Tamim", "Nahid", "Rajon"]
print(we)
we.append("Nasim")
print(we)
we.append("Tanvir")
print(we)

# sort()-----
we = ["Arif", "Ayon", "Nazim", "Tamim", "Nahid", "Rajon"]
we.sort()
print(we)

num = [1, 5, 8, 6, 2, 7, 9, 3, 4]
num.sort()
print(num)

# reverse()--------
reve = [1, 2, 3, 4, 5]
reve.reverse()
print(reve)

# insert()----
we = ["Arif", "Ayon", "Tamim", "Nahid", "Rajon"]
we.insert(5, "Nazim")
print(we)

# remove()---------
we = ["Arif", "Ayon", "Tamim", "Nahid", "Rajon"]
we.remove("Nahid")
print(we)

# pop()----------
we = ["Arif", "Ayon", "Tamim", "Nahid", "Rajon"]
we.pop(1)
print(we)
we.pop(3)
print(we)

# extend()----------
li = [1, 2, 3]
li2 = [3, 4, 5]
li.extend(li2)
print(li)

# count()----------
li = [1, 2, 3, 3, 4, 5, 6]
co = li.count(3)
co2 = li.count(4)
print(co)
print(co2)

# del()---------
li = [1, 2, 3, 3, 4, 5, 6]
del(li[0])
print(li)

# li []------
li = []
for x in range(10):
    li.append(x)

print(li)

# +, * == ?
li1 = [1, 2, 3]
li2 = [4, 5, 6]
li = li1 + li2
print(li)

# +, * == ?
li1 = [1, 2, 3]
li2 = li2 * 3
print(li2)

# join()--------
li = ["a", "b", "c"]
print(li)

str = ",".join(li)
print(str)

str = " - ".join(li)
print(str)

# List Comprehensions---------
li = [1, 2, 3, 4]
new_li = []
for x in li:
    new_li.append(2 * x)

print(new_li)

# List Comprehensions---------
new_li = [3 * x for x in li]
print(new_li)

# List Comprehensions----Even-----
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_number = []
for x in li:
    if x % 2 == 0:
        even_number.append(x)

print(even_number)

# List Comprehensions----Odd-----
even_number = [x for x in range(1, 11) if x % 2 == 0]
print(even_number)

# List Comprehensions----Odd-----
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_number = []
for x in li:
    if x % 2 != 0:
        odd_number.append(x)


print(odd_number)

# List Comprehensions----Odd-----
odd_number = [x for x in range(1, 11) if x % 2 != 0]
print(odd_number)


# ------------End------------- #
