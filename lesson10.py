# 24/12/2020-------
# Tamim Shahriar Subeen-------
# Python Data Structure----------------
# Dictionary[]----------

marks = [78, 72, 68, 80, 63, 75]
roll = input("Please enter your roll number: ")
print("Your marks is", marks[int(roll)-1])

# Dictionary[]----------
marks = [78, 72], [68, 80], [63, 75]
print(marks[1])
print(marks[2][1])

# Dictionary[]----------
marks = {1: 78, 2: 72, 3: 68, 4: 80, 5: 63, 6: 75}
print(type(marks))
print(marks[5])
print("Marks of roll number 3 is", marks[3])

# Dictionary[]----------
marks = {1001: 75, 1002: 72, 1003: 77, 1004: 84}
print(marks[1003])

# Dictionary[]----------
marks = {"DH1001": 75, "DH1002": 67, "DH1003": 76, "DH1004": 68}
print(marks["DH1002"])

# Dictionary[]----------
dt = {}
print(dt)
print(type(dt))

# Dictionary[]----------
dt[1] = "One"
print(dt)
print(dt[1])
dt[2] = "Two"
print(dt)
print(dt[2])

# Dictionary[]----------
dt = {"a": "A", "B": "b", "C": "c"}
print(dt)
print(dt["C"])

# Dictionary[]----------
dt = {"a": "A", "B": "b", "C": "c"}
dt[(1, 2, 3)] = 'tuple'
print(dt)

# Dictionary[]----------
marks00 = {"DH1001": {"Bangla": 75, "English": 77}, "DH1002": {"Bangla": 88, "English": 68}, "DH1003": {"Bangla": 66, "English": 88}}
print(marks00)
print(marks00["DH1003"])
print(marks00["DH1003"]["English"])

bd_divition_info = {}
bd_divition_info["Barishal"] = {"district": 6, "upazila": 39, "union": 333}
print("\n")
bd_divition_info["Chittagong"] = {"district": 11, "upazila": 97, "union": 336}
print("\n")
bd_divition_info["Dhaka"] = {"district": 13, "upazila": 93, "union": 1833}
print("\n")
bd_divition_info["Khulna"] = {"district": 10, "upazila": 59, "union": 270}
print("\n")
bd_divition_info["Mymensing"] = {"district": 4, "upazila": 34, "union": 350}
print("\n")
bd_divition_info["Rajshahi"] = {"district": 8, "upazila": 70, "union": 558}
print("\n")
bd_divition_info["Rangpur"] = {"district": 8, "upazila": 58, "union": 536}
print("\n")
bd_divition_info["Sylhet"] = {"district": 4, "upazila": 38, "union": 334}
print(bd_divition_info)
print(bd_divition_info["Khulna"])

divitions = bd_divition_info.keys()
print(divitions)

for divition in divitions:
    print(divition, "Divition")

for divition in divitions:
    print(divition, "upazila", bd_divition_info[divition]["upazila"])
#   print(divition, "union", bd_divition_info[divition]["union"])
#   print(divition, "upazila", bd_divition_info[divition]["upazila"], "union", bd_divition_info[divition]["union"])

print("Using item--------------------")
for item in bd_divition_info:
    print(item)

print("Using item--------------------")
for key in bd_divition_info:
    print(key)
    print(bd_divition_info[key])

print("Using key and value--------------------")
for key, value in bd_divition_info.items():
    print(key)
    print(value)


# ------------End------------- #
