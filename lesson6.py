# 24/12/2020-------
# Tamim Shahriar Subeen-------
# String()----------------

s = "hello"
print(len(s))
print(s)

l = len(s)
print(l)

s = ''
print(s)
print(len(s))

s = "Dimik's"
print(s)

s = "Dimik\s"
print(s)

country = "Bangladesh"
print(country[4])

for c in country:
    print(c)

c = ["A", "b", "c"]
print(c)
print(c[1])


country2 = "Bangl" + "adesh"
print(country2)
x = "50" + "5"
print(x)

country3 = "Bangldesh"
print(country.find("Ban"))
print(country.find("ang"))
print(country.find("Bangla"))
print(country.find("Bengla"))
print(country3.find("desh"))

country4 = "North Korea"
new_country4 = country4.replace("North", "South")
print(country4)
print(new_country4)

text = "this is a test. this is another test. this is final test."
new_text = text.replace("this", "This")
print(text)
print(new_text)


text2 = "hello"
text2 = text2.replace("hello", "Hello")
print(text2)

text3 = " this is a string. "
print(text3)
t1 = text3.lstrip()
print(t1)
t2 = text3.rstrip()
print(t2)

t3 = text3.strip()
print(t3)

text4 = " this is a sentence. "
new_text4 = text4.rstrip()
print(new_text4)
print(text4)

s1 = "Arif"
s_up = s1.upper()
print(s_up)

s_lw = s1.lower()
print(s_lw)

s_cap = s1.capitalize()
print(s_cap)


str = "I am a programmer"
words = str.split()
print(words)

for word in words:
    print(word)


str2 = "This is"
str2 = str2.count("is")
print(str2)

s2 = "Arif"
po = s2.startswith("Ari")
print(po)

po = s2.startswith("ari")
print(po)

po = s2.endswith("if")
print(po)

po = s2.endswith("f")
print(po)

name = "Mr. Arif Billah"
if name.startswith("Mr."):
    print("Dear Sir")

str3 = "a quick brown for jumps over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, str3.count(c))


import turtle
name = turtle.textinput("name", "what is your name?")
name = name.lower()
if name.startswith("mr"):
    print("Hello Sir, how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello Madam, how are you?")
else:
    name = name.capitalize()
    str = "Hi " + name + "!How are you?"
    print(str)

turtle.exitonclick()


# ------------End------------- #
