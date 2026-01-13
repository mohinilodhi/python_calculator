#addition for this
x=4
y=6

print("the addition of",x+y,"okay")

name = "mohini"#how to print in python
print("hello world")
print("i am mohini lodhi from aiml section c")
print("HEY EVERYONE YOU ALL GUYS ARE VERY AMAZING AND VERY GOOD LOOKING I LIKE YOU VERY MOST BROO EVERYONE YOU ARE ")

#HEY HARRY IS MY NAME 
a = 1.56789
b = True
c = "harry"
d = None
print(a)
print(b)
a1 = 9
print(a+a1)
print("the type of a is", type(a))
print("the type of b ",type(b))
print("the type of c is ", type(c))

list1 = [2,345,67,[-5.6]],["apple","grapes","banana"]
print(list1)

tuple = ("lion","tiger","parrot")
print(tuple)


#condition
o=567
if(o<600):
    print(" o is greater than 600")
    print("add to cart please")
else:
    print("o is not greter than 600")
    print("please do not add the cart this please")


#diictionary
dict1 = {"name":"sakshi","age":67}
print(dict1)

n=13
m=12
ans1 = n+m
print("addition of", n + m,"is" ,ans1)


#input
a = input()
print("my name is narry",a)

x = input("enter your first number:")
y = input("enter your second number:")

print(x+y)
print("hello",name)


#string slicing
fruit = "mohini"
len = len(fruit)
print("mango is a",len,"letter word")

pie = "applepie"
print(pie[0:5])


a = "priya"
for i in a:
    print(i)

#strings are immutable

str = "AHSHSJhsjhsjshjjk"
print(str.upper())
print(str.lower())
print(str.rstrip("!"))

str2 = "silver spoon"
print(str2.replace("sp","m"))
print(str2.split(" "))

capstr = str.capitalize()
print(capstr)
str2 = "hello world"
capstr = str2.capitalize()
print(capstr)

num = int(input("enter the value of num:  "))
if(num<0):
    print("number is negeative")
elif(num==0):
    print("number is zero")
elif(num==999):
    print("number is zero")
else:
    print("this number is zero")

print("this is my new number please save this number ")

#condition
book=200
money=34
if (book<=money):
    print("alexa do not book any book for me")
else:
    print("alexa please do not save this okay i really donot want this number")

#shortcut for list
nums =[i*i  for i in range(1, 6)]
print(nums)


#exception handling
try:
    x = int(input("Enter number: "))
    print(10/x)
except ZeroDivisionError:
    print("do not divide with zero")
except ValueError:
    print("do not enter invalid values")
else:
    print("no error")
finally:
    print("done")


print("thankyou so much for watch this")