'''

a, b = 78
print(a, b)


a=7, 8
print(a)
print(type(a))


a=b, c=4, 2
print(a,b,c)


-----> changing variables
eg:1
a=7
b=5
temp=a
a=b
b=temp
print(a, b)


eg:2
a=7
b=5
a=a+b
b=a-b
a=a-b
print(a, b)


eg:3
a=7
b=5
a, b=b, a
print(a,b)


eg:4
a=7
b=5
a=a*b
b=a/b
a=a/b
print(int(a),int(b))


--->used to find the memory adress of the variable
a=7
b=8
print(id(a))
print(id(b))



-->Keywords
keywords are preserved words which provides special meaning to compiler or interchanger

import keyword
print(keyword.kwlist)

'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
<class 'list'>


import keyword
print(keyword.is keyword("kousik"))

False


#--->Literals
Literal is the constant value assigned to a variable
A variable is considers to be constant when it is defines
in caps

a=78 # a nis variable
A=78 # A uis constant


l1 = [9,8,0]
l1 = [6, 7, 8, 0]
l1 = 89


hash()---> it creates a hask value for constant datatypes anfd provides error for non constant sata types

n1=89+7j
print(hash(n1))

7000110

f1=[7,8,9]
print(hash(f1)) #error ---> list is non-constantor multiple datatype

7000110
6950854851967187257

a=9
b=9
b=90
print(id(a))
print(id(b))

140721710189240
140721710191832

#!--->Operators
?operators are symbols which is used to perform various oprations b/w 2 or more operands 

Arthematic
Assignement
Logical
relational or comparision
bitwise
identity
membership

# *---> Arthematic ---> +,-,*,/,%,//,**

eg:1
a=8
b=6
c=9
print(a+b+c)

23

#input() --> used to get the routine input
n1=input("Enter the value:")
print(n1)

https://medium.com/@a.tavallaie/python-programming-libraries-for-mechanical-engineer-409cf994efdd

a=4
b=2
print(a/b) # is used to get the quopient value
print(a%b) # is used to get the remainder value

# ! // --> Floor devison

a= 765433
b=19
print(a//b)

40285
#--> the output will be in integer & the output will be based on floor value

#!---> used fro power number
print(2**4)

16

# ! --->  Assignment

a=8
a+=2
print(a)

10

a=30
a-=5
print(a)

25

# comparison----> ==, >,<,!=,<=,>=

a=8
b=7
print(a>b)

True

a=9
b=5
print(a==b)

False

# ! Bitwise operator ---> &,|,^,~,<<,>>

a=7
b=4
print(a&b)

4


# AND
 A B A&B
 0 0  0
 0 1  0
 1 0  0
 1 1  1

# OR
 A B A|B
 0 0  0
 0 1  1
 1 0  1
 1 1  1

# XOR 
 A B A^B
 0 0  0
 0 1  1 
 1 0  1
 1 1  0

 32 16 8  4 2 1
 0  0  1  0 1 0 #--> 10
 1  0  0  1 1 0 #--> 38
--------------------------
 1     1  1

print(10^38)

# 2^4 2^3 2^2 2^1 2^0
   8   4   2   1

   0   1   1    1  # -->7
   0   1   0    0  # --> 4 &
-------------------------
   0   1   0    0

# ~ --->
a= 9876
print(~a)

-9877

a=9

128 64 32 16 8 4 2 1
0   0   0  0 1 0 0 1 #---> 9

1   1   1  1 0 1 1 0 #---> -10


0   0   0  0 1 0 1 0 #---> 10

1 1 1 1 0 1 0 1 0 --> 1 st compliment of 10
                1 -->2 nd compliment
---------------------------------------
1   1   1  1 0 1 1 0 #---> -10


#---> <<,>>

print(5<<3)

40

# ! Logical
and, or, not

a=6
print(a>3 and a<10)

True

a=6
print(a>7 and a<30)

False

a=6
print(not(a>8 and a<10))

True

# ! Identity of vector
it is used to compare the memory location are stored

is, is not

a=8
b=8
print(a is b)

True

print(a==b)

True

a=[1,2,3]
b=[1,2,3]
print(a is b)

False

a=(1,2,3)
b=(1,2,3)
print(a is b)

True

# ! ---> Membership operator
   in, not in
   
L1=[7,8,9,0,6,5]
num=55
print(num in L1)

False

print(num not in L1)

True

num=678
print(8 in num)

Traceback (most recent call last):
  File "C:\Users\Admin\Desktop\python\day 2.1.py", line 326, in <module>
    print(8 in num)
TypeError: argument of type 'int' is not iterable

# ! conditional statement
  if, elif, else


python syntax
if condition:
    statement
    statement
    statement
    statement


eg:1
a = 6
if a:
    print("hello")

#Eg:2

a=6
if a>3:
    print("hey")
else:
    print("no")

#Eg:3
if 7>8:
    print("kousik")
else:
    print("no")



n=int(input("enter the number"))
if n %2==0:
      print(n, "is even")
else:
    print(n, "is odd")
      
'''


