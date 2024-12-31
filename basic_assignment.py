# 1)take input from user and print its inputvalue using input function
a=int(input('Enter your value :'))
print(a),  # Output: (Depends on input)

#2)create a string and print the last element 
a='itvedant'
print(a[-1])  # Output:t#

#3)create a string and print second last element
a='itvedant'
print(a[-2])  # Output:n

#4)create a string as eg:"hellohellohellohello" and print it 
a=('hello'+'hello'+'hello'+'hello')
print(a)  # Output: hellohellohellohello

#5)create  two string like "hello" and "world" and print "helloworld"
a=('hello'+'world')
print(a)  # Output:helloworld

#6)create two variable and swap its value eg a=10,b=20 afer swapping there output is a=20,b=10
a=10
b=20
a,b=b,a
print(a,b)  # Output:20,10

#7)create a tuple like(1,2,3,4,3,2) and count number of  occurrences  of 3
a=(1,2,3,4,3,2)
b=a.count(3)
print(b)  # Output:2

#8)create a tuple like(1,2,3,4,3,2) and print the index number of 3
a=(1,2,3,4,3,2)
print(a.index(3))  # Output:2

#9)create a tuple like(1,2,3,4,3,2) and print (2,3,4) only
a=(1,2,3,4,3,2)
print(a[1:4])  # Output:(2, 3, 4)

#10)create tuple like(1,2,3,4,3,2) and remove 3 in this tuple

tpl = (1, 2, 3, 4, 3, 2)

# Convert tuple to list
lst = list(tpl)

# Remove the first occurrence of 3
lst.remove(3)

# Convert the list back to tuple
tpl = tuple(lst)

print(tpl)  # Output: (1, 2, 4, 3, 2)



#11)create a list like[1,2,3,4] and change the elements like[1,2,4,3] without using list methods
list=[1,2,3,4]
list[2],list[3]=list[3],list[2]   # Using swapin 
print(list) # Output: [1, 2, 4, 3]

#12)create a list like[1,2,3,4] and delete all the elements in list and print empty list without using any method 
list=[1,2,3,4]
list.clear()
print(list) # Output:[]


#13)create single value tuple 
t=(1,)
print(type(t)) # Output:<class 'tuple'>

#14)create empty set
a=set()
print(type(a)) # Output:<class 'set'>

#15)create a dictionery like {"a":10,"b":20} and print the value of "a" without using methods

d={"a":10,"b":20}
print(d['a']) # Output:10

#16)create a dictionery like {"a":10,"b":20} and change the value of "b" is 30 and print it without using methods
d={"a":10,"b":20}
d['b']=30
print(d) # Output:{'a': 10, 'b': 30}


# 17)create a dictionery like {"a":10,"b":20} and insert the key value pair which the key is "c" and the value is 30 and print it
dict={"a":10,"b":20}
dict['c']=30
print(dict) # Output:{'a': 10, 'b': 20, 'c': 30}

#18)create two sets like {1,2,3,4} and {3,4,5,6} and find the union without using union method
a={1,2,3,4}
b={3,4,5,6}
union=a|b
print(union) # Output:{1, 2, 3, 4, 5, 6}

#19) create two sets like {1,2,3,4} and {3,4,5,6} and find the intersection without using intersection method
a={1,2,3,4}
b={3,4,5,6}
intersection=a&b
print(intersection) # Output:{3, 4}


#20)create two sets like {1,2,3,4} and {3,4,5,6} and find there difference without using difference method

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = {x for x in set1 if x not in set2}
print(difference)  # Output: {1, 2}


#21)create a set like {1,2,3,4} and remove 3 

set1 = {1, 2, 3, 4}
set1.remove(3)
print(set1)  # Output: {1, 2, 4}


#22)create a set like {1,2,3,4} and remove 3 using discard method and undrstand what's the difference between remove and pop

set1 = {1, 2, 3, 4}
set1.discard(3)
print(set1)  # Output: {1, 2, 4}

# Difference:
# - `remove` raises an error if the element is not found.
# - `discard` does nothing if the element is absent.


#23)create a string like "hello world" and count "o"

string = "hello world"
count_o = string.count("o")
print(count_o)  # Output: 2


#24)create a string like "hello world" and find "z" or index "z" and understand difference between index and count

string = "hello world"

# Find index of 'z'
try:
    index_z = string.index("z")  # Raises error if not found
except ValueError:
    index_z = "Not found"

print(index_z)  # Output: Not found

# Difference:
# - `index` raises an error if the character is not found.
# - `count` returns 0 if the character is not found.


#25)create a list like ["p","y","t","h","o","n"] and print "python"

lst = ["p", "y", "t", "h", "o", "n"]
string = "".join(lst)
print(string)  # Output: "python"


#26)create a string "python" and print ["p","y","t","h","o","n"]

string = "python"
lst = list(string)
print(lst)  # Output: ["p", "y", "t", "h", "o", "n"]


#27)create a string like"     python" and print "python"

string = "     python"
trimmed = string.strip()
print(trimmed)  # Output: "python"


#28)create a list [1,2,3,4] and print it like [1,2,3,4,5]

lst = [1, 2, 3, 4]
lst.append(5)
print(lst)  # Output: [1, 2, 3, 4, 5]


#29)create a list [1,2,3,4] and print [1,2,3,4,1,2,3,4] using extend function

lst = [1, 2, 3, 4]
lst.extend(lst)
print(lst)  # Output: [1, 2, 3, 4, 1, 2, 3, 4]


#30)create a list [1,2,3,4] and print [1,2,3,4,"p","y","t","h","o","n"] using extend function

lst = [1, 2, 3, 4]
lst.extend(["p", "y", "t", "h", "o", "n"])
print(lst)  # Output: [1, 2, 3, 4, "p", "y", "t", "h", "o", "n"]


#31)create a list [1,2,3,4] and remove 2 using pop function

lst = [1, 2, 3, 4]
lst.pop(1)  # Removes element at index 1
print(lst)  # Output: [1, 3, 4]


#32)create a list [1,2,3,4] and print [1,5,3,4] using insert function

lst = [1, 2, 3, 4]

# Positive indexing
lst.insert(1, 5)  # Insert `5` at index 1
print(lst)  # Output: [1, 5, 2, 3, 4]



#33)create a list [1,2,3,4] and print [1,5,3,4] using negative indexing in insert function

lst = [1, 2, 3, 4]
lst.insert(-3, 5)  # Negative index for position
print(lst)  # Output: [1, 5, 2, 3, 4]


#34)create a list [1,2,3,4] and print [4,3,2,1]

lst = [1, 2, 3, 4]
lst.reverse()
print(lst)  # Output: [4, 3, 2, 1]


#35)create a list [1,4,3,2] and print [1,2,3,4] using function

lst = [1, 4, 3, 2]
lst.sort()
print(lst)  # Output: [1, 2, 3, 4]


#36)create a dict {"a":10,"b":12,"c":14} and clear it{}

dict1 = {"a": 10, "b": 12, "c": 14}
dict1.clear()
print(dict1)  # Output: {}


#37)create a empty set{}

empty_set = set()

#38)create empty dict{}
empty_dict = {}

#39)create a dict{"a":10,"b":20,"c":30} and print {"b":20,"c":30}

dict1 = {"a": 10, "b": 20, "c": 30}
filtered = {k: v for k, v in dict1.items() if k != "a"}
print(filtered)  # Output: {"b": 20, "c": 30}


#40)create a set {1,2,3,4} and remove 2

set1 = {1, 2, 3, 4}
set1.remove(2)
print(set1)  # Output: {1, 3, 4}
