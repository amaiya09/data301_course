print("I can start coding!")

print("I know that I can program in Python.")
print("I am programming right now. ")
print("My awesome program has three lines!")

a = """
I know that I can program in Python.
I am programming right now.
My awesome program has three lines!"""
print(a)

######################################
######################################


print(35 + 5 * 10)

num = 10 ** 2 -9 % (3+1)
print(num)

name = "Irene"
height = '''5'1"'''
print(name)
print(height)
print("name:",name,"height:", height)


###############################################
# Try it: Python String Variables and Functions
###############################################


name = "Joe"
age = 25
print("Name: "+name)
print("Age: "+str(age))

name = "Steve Smith"
print("First Name: "+name[0:5])
print("Last Name: "+name[6:])

twonames = name.split()
print("First Name: "+twonames[0])
print("Last Name: "+twonames[1])

# Alternative answer
# the find() function can find space so that it works with all names.
loc = name.find(" ") # 5
print("First Name: "+name[0:loc])
print("Last Name: "+name[loc+1:])


###############################################
# Try it: Python Input, Output, and Dates
###############################################

# 1)
name = input("What is your name?")
print("Your name is: "+name)
print("Length:",len(name))
print("First five characters: "+name[0:5])

# Note: Used comma syntax instead of concatenation.  If concatenate, then need to convert using str().

# 2) 
from datetime import datetime
current = datetime.now()
print("{}/{}/{}".format(current.year, current.month, current.day))

# Note: To get it to have a leading zero will need to look at strftime method:
print(current.strftime("%Y/%m/%d"))


###############################################
# Try it: Decisions
###############################################



# 1)
num = input("Enter a number: ")
if int(num) % 2 == 0:
    print("even")
else:
    print("odd")

# 2)
num = input("Enter a number: ")
n = int(num)
if n == 1:
    print("one")
elif n == 2:
    print("two")    
elif n == 3:
    print("three")
elif n == 4:
    print("four")
elif n == 5:
    print("five")
else:
    print("error")
    
    
    
###############################################
# while loops
###############################################

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"
    
    
###############################################
# Question: for loops
###############################################

    
for i in range(11,0, -1):
 	print(i)


###############################################
# Try it: for loops
###############################################

# 1)
for i in range(1, 11, 1):
 	print(i)
for i in range(10, 0, -1):
 	print(i)

# 2)
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print(n)

#More efficient:
for n in range(15,91,15):
    print(n)

# 3)
total = 0
maxnum = 0
for i in range(1,6):
    n = input("Enter a number: ")
    n = int(n)
    total += n
    if n > maxnum:
        maxnum = n

print("Max:",maxnum)
print("Sum:",total)
print("Avg:",total/5)



###############################################
# Retreiving items from a list:
###############################################

for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

# List concatenation using +
# x + y
# for two lists x and y

letters = ['a', 'b', 'c', 'd']
print(" ".join(letters))
print("---".join(letters))
#  In the example above, we create a list called letters.
#  Then, we print a b c d. The .join method uses the string to combine the items in the list.
#  Finally, we print a---b---c---d. We are calling the .join function on the "---" string.
#  We want to turn each row into "O ".


###############################################
#  list operations
###############################################

reversed(list.sort()) - will put in reverse order
list.sort(reverse=True)

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b, in zip(list_a, list_b):
    if a>b:
        print(a)
    else:
        print(b)


###############################################
#  Try it: lists
###############################################

#Question 1: Write a program that puts the numbers from 1 to 10 in a list then prints them by traversing the list.
data = []
for i in range(1, 11, 1):
    data.append(i)
for v in data:
    print(v)


#Question 2: Write a program that will multiply all elements in a list by 2.
data = list(range(1,11))

for idx, val in enumerate(data):
    data[idx] = val * 2

print(data)


#Question 3: Write a program that reads in a sentence from the user and splits the sentence into words using split().  Print only the words that are more than 3 characters long.  At the end print the total number of words.
# A frog and a hog cavort in the bog. But not the hippopotamus
sentence = input("Enter a sentence: ")
words = sentence.split()
for w in words:
    if len(w) > 3:
        print(w)
print(len(words))



#Counter will create a dictionary from a list that has the keys and the frequency of their occurrence.
from collections import Counter
data = [1,1,3,2,3,1]
c = Counter(data)
print(c)  #  Counter({1: 3, 3: 2, 2: 1})
for n, count in c.most_common(5):
    print(n, count)

#Data structure set will remove duplicates.
s = set(data)



###############################################
#  Try it: dictionary
###############################################

import string
counts = {}
for letter in string.ascii_uppercase:
    counts[letter] = 0
print(counts)



# 1)
from pprint import pprint

# Alternative way to build dictionary
#counts = {}
#for l in range(65,91):
#	counts[chr(l)] = 0

import string
counts = {}
for letter in string.ascii_uppercase:
    counts[letter] = 0
print(counts)


str = input("Enter a message: ")
# A hog and a frog cavort in a bog but not the hippopotamus 
str = str.upper()
for c in str:
    if c in counts:
        counts[c] = counts[c]+1
print(counts)
pprint(counts)


###############################################
#  Practice Questions: Functions
###############################################


def doubleNum(num):
    num = num * 2
        print("Num: "+str(num))
        return num
n = doubleNum(5)						# 10
print(str(doubleNum(n)))


##################
# lambda function
##################

# SYNTAX:
# lambda arguments : expression
x = lambda a, b : a * b
print(x(5, 6))


# 1)
def largest(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
print(largest(10,15))
print(largest(5,5))

# 2)
def printN(n):
    for i in range(1,n+1):
        print(i)
        
printN(10)

