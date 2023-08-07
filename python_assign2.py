#1.1 Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))  


#2.Write a program which can compute the factorial of a given numbers.

n = int(input()) 
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
 

 #3. {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input())
d = dict()
for i in range(1,n+1):
    d[i] = i * i
print (d) 

 
#4. 34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

inp = input()
lst = inp.split(",")
tpl = tuple(lst)
print ("list is: " ,lst)
print ("Tuple is:" ,tpl)

"""5 Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case."""

class Sample():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

obj = Sample()
obj.get_string()
obj.print_string() 

""" 6.Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence."""

from math import sqrt
C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

print(",".join([str(int(calc(int(i)))) for i in input().split(',')])) 


#7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j 

x,y = map(int,input().split(','))
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)

#8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

lst=input().split(',')
lst.sort()
print (','.join(lst)) 


#9.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized

lst = []

while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x.upper())

for line in lst:
    print(line) 


#10.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

word = sorted(list(set(input().split())))              
print(" ".join(word))


 #11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))


#12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2 == 0) and (int(s[1])%2 == 0) and (int(s[2])%2 == 0) and (int(s[3])%2 == 0):
        values.append(s)
print (",".join(values)) 

#13.Write a program that accepts a sentence and calculate the number of letters and digits.

s = input()
d = {"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"]) 

#14.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

s = input()
d = {"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("UPPER CASE", d["UPPER CASE"])
print ("LOWER CASE", d["LOWER CASE"])


#15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)


#16.Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))