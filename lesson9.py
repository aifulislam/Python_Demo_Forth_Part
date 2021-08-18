# 24/12/2020-------
# Tamim Shahriar Subeen-------
# Python Data Structure----------------
# Set{}----------

A = set()
print(type(A))

items = {"Arif", "Ayon", "Nazim", "Tamim", "Nahid", "Rajon"}
print(items)
print(type(items))

li = [1, 2, 3]
tp1 = (1, 2, 3)
A = set(li)
print(type(A))
B = set(tp1)
print(type(B))

A = set("Bangladesh")
s = {'e', 'g', 'h', 'a', 's', 'l', 'B', 'd', 'n'}
print(s)
print(type(s))
p = {1, 2, 3}
if 2 in p:
    print(True)
else:
    print(False)

m = {1, 2, 3, 4, 5}
n = {2, 4, 6, 8}
v = m & n
# v = m | n
# v = m ^ n
# v = m - n
# v = n - m
print(v)


# ------------End------------- #
