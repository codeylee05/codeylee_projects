
##DATA TYPES##

#int (whole positive or negative number)

#float (with decimal point)

#string ("")

#bool (True(1) or False(0))

##PRINT##

#print() (outputs something on console)

print("Hello World")
print("Hello", "Lefa", end = '|' )
print("How are you today?", end = '|') #end = '|' means the print line should end with | but that means the next print line will commence on the same console line

print("I am good thanks")
print("Bye", end = '\n') #end = '\n' means the the next print line should begine on the next console line
print("Bye bye")

##VARIABLES##

x = "Lefa"
y = "Mofokeng"
print(x, y)
x = y #reassigning a variable(in this case to another variable)
print(x)

#we cannot start a variable with number
#we can use the underscore in variable names

#Casting is when we specify the data type of a variable
x = str(3)
y = str(3)
z = float(3)
#when we print the variable, it will printed as the data type assigned to it

##INPUT##

name = input("Name: ") #assigning a variable to the input
print(name)

details = input("Age: ")
print("The user, ", name, details, "is approved") #combining strings and variables

#ARITHMETICS#

x = 10
y = 5
result = x + y
result = x - y
result = x * y
result = x / y

result = x ** y #to the power of
result = x // y #(floor division) gives integer result of division
result = x % y #(mod) returns remainder of division

#Python follows BEDMAS order of operation by default but you can use brackets to perform calculations in specific way

num = input("Number: ")
#the program always returns the input as a string so we will have to convert it to a number before arithemtic operations
print(int(num) - 5) #converts num to int
print(float(num) - 5) #converts num to float

##METHODS AND TYPES#

hello = "hello world"
print(type(hello)) #tells us of what class is the variable 'hello' an instance of(in this case it is an instance of class string)
hello = 5
print(type(hello)) #(in this case it is an instance of class integer)

hello = "hello world"
print(hello.upper()) #so the method .upper will act on the object 'hello world' of the class string(only bcoz the method is atrributable to the class string)
hello = "heLLo world"
print(hello.count('L')) #so the method .count will act on the object 'heLLo world' to count how many occurrences of 'L' are there(in this case there are 2 occurences )

##STRING & INT ARITHMETICS##

x = "Lee"
y = 3
print(x * y)
#we can multiply int and string(hence it will print 'Lee' 3 times)

x = "Lee "
y = ",the world's greatest coder"
print(x + y)
#we can add[concatenate] two strings together for they are the same class

##CONDITIONAL OPERATORS##

#the result of a conditional operator is a boolean(bool) so True or False
'''
== #is equal to
!= #is not equal to
<= #is lesser than or equal to
>= #is greater than or equal to
< #lesser than
> #greater than 
'''

print("a" > "Z") #will print a bool based on if the ordinal number(ASCII) for 'a' is larger than that for 'z'
print("ab" > "ad") #will print a bool based on if the sum of ordinals for 'ab' are bigger than those for 'ad'

result = 6 == 6
print(result) #will print object of the variable 'result' which is on this case a bool of whether 6 is equal to 6

##CHAINED CONDITIONALS##

x = 5
y = 2
z = 4

result1 = x == y
result2 = y > x
result3 = z < x + 2

#OR#
result4 = result1 or result2 or result3 #if atleast one bool or all were True, the bool for 'result4' will be True also
print(result4) 

result4 = result1 or not result2 or result3 #it will evaluate the bool of 'result2' and inverse it (so False changes to True and vica versa)
print(result4)

#NOT#
print(not True) #the bool True is inversed to False
print(not False) #the bool False is inversed to True
print(not (False or True)) #one of the bools is True hence the conditional is evaluated as True and so the bool is inversed to False

#AND#
print(False and False) #the conditional will only output True if both bools are True 
print(False and True)
print(True and True)

#order of evaluation is NOT AND OR

print(True and False or True) #and evaluates False then or evaluates True
print(not (True and False or True)) #within the brackets, and evaluates False then or evaluates True, outside brackets, not evaluates false

##IF ELIF ELSE##

x = input("Name: ")

if x == "Lefa":
    print("You are the greatest at Python!")
elif x == "Tim":
    print("You are a great Python teacher")
else:
    print("You suck")

##LIST/TUPLES##

#Lists are mutable(we can append, remove, change elements)
x = [4, "hello", True] #we can assign a variable to a a collection type known as a list (we can just leave the list empty)
print(len(x)) #the len() function outputs how many elements are in the list

x.append("bye") #the method. append acts to add an element to the list assigned to x
print(x)

x.extend([5, 10, "lovey", False]) #the method .extend acts to add more elements to the list assigned x
print(x)

print(x.pop()) #the method .pop acts remove and return the final element in the list assigned x
print(x) #now the list will be printed without the popped element
print(x.pop(0)) #now the argument of the .pop method is the index 0 hence the first element is popped

print(x[1]) #the element of index 1 is printed

x[0] = "hey" #hence the element of index 0 will be changed from one element to another
print(x)

#Tuples are immutable(we cannot append, remove, change elements)
x = () #tuples are characterized by curve brackets

#You can have lists/tuples inside of lists/tuples

##LOOPS##

#WHILE LOOP: We dont know how many times the code will run
#FOR LOOP: We definitely know how many times it will run

for i in range(10):
    print(i) #for the variable being in range of (argument), print the possible values of the variable

#the position of an argument of the range()function determines the how the function will operate  
#range(x) -> stop at x(but not include) (the range will begin with 0)
#range(x,y) -> start at x, stop at y(but not include)
#range(x,y,z) -> start at x, stop at y(but not include), step(+/-) by z

for i in range(10): #the program stops at 10(but does not include)
    print(i)

for i in range(5, 10): #the program starts at 5 and stops at 10(but not include)
    print(i)

for i in range(10, -1, -2): #the program starts at 10, stops at -1(but not include), steps by -2 
    print(i)

x = [8, 4, 45, 18, 101]

for i in x:
    print(i)
#or
for i in range(len(x)): #the program will evaluate how many elements are in x and that quantity will be the range by index
    print(x[i]) #so if len(x) is 5, elements of index 1 up to index 5 will be printed as 'i'

for i, element in enumerate(x): 
    print(i, element) #the program will print each index nr. with the corresponding element for the set x

i = 0
while i < 10:
    print("run")
    i += 1 #or alternatively [i = i + 1]
#alternatively;
while True:
    print("run")
    i += 1  
    if i == 10:
        break 

##SLICE OPERATOR##

##'variable' = [:::] #[start:stop:step]

x = [0, 1, 2, 3, 4, 5, 6, 7,]
sliced = x[0:4:2] #"start at 0, go to but not include 4, step by -2"
sliced = x[:4] #just stop at 4(bni) so automatically starts at 0(index 0)
sliced = x[4:] #just start at 4, so automatically stops at 7(final index)
sliced = x[0:4:] #just start 0, stop at 4(bni), so automatically steps by 1
sliced = x[::-1] #just start at 0, stop at 7, step by -1 (so the elements in the list are reverse ordered)

y = "hello world"
sliced = y[::-1] #the string is reversed

#the sliced operator can also work on tuples

##SETS##

##a set is an unordered unqiue collection of elements. We dont care about frequency or order of elements
##so using sets is very fast. We use them only if we care that something exists and not the order or frequency

x = set() #we need to state the class set() if we are gonna leave the set empty otherwise
x = {4, 15, 73, 0, 3, 3, 67, 84, 0} #we can use {} if we are gonna inmediately place something in the set
y = {"fun", 50, 79, 19}

print(x) #the set will be printed regardless of order and duplicates will not be printed
##Operations with Sets
x.add(10)
x.remove(3)

print(15 in x) #to check if an element is in the set [in this case: True]
print(x.union(y)) #to unite two sets [so the method .union will join set 'y' to set 'x']
print(x.difference(y))
print(x.intersection(y))
#etc methods...

##a program wil execute much faster with sets than lists

##DICTIONARIES##

##a dictionary is a key-value pair {'key': value assigned to key}

#the key can be anything
x = {'k': 10}
print(x)

x['k2'] = 5 #to add a key with an assigned value or assign a new value to a key
print(x)

print('k' in x) #to check if the value assigned key 'k' is in the dict
print('k3' in x) #[false as there is no key 'k3']

print(list(x.values())) #will print all the dict values of set x
print(list(x.keys())) #will instead print all the keys of set x
#note that list() will return the output as a list []

del x['k'] #so the key 'k' and its assigned value are deleted
print(x)

for key, value in x.items(): #too loop through all dict items of x and return each key and assigned value
    print(key, value)
for key in x:
    print(key) #the program will print just the keys of dict x
for key in x:
    print(key, x[key]) #the programm will print each key along with its assigned value

##COMPREHENSIONS##

x = [x for x in range(100)] #outputs a value for x in range 0 to 100(bni) (100 times)
y = [[0 for y in range(100)] for y in range(5)] #outputs a value for x = 0 in range 0 to 100(bni) all in range 0 to 4 (5 times)
print(x)
print(y)

##FUNCTIONS##

def func(x, y):
    print(x, y) #so when function is called, the values assigned to the arguments will be printed
    return x * y #so when function is called within print statement, the values assigned to arguments will be multiplied

func(10, 3) #calling the function
print(func(20, 6)) #calling the function within the print statement

def func2(x, y):
    return x * y, x + y

print(func2(7, 5))
#the output will be as a tuple (). We can unpack this tuple by;
r1, r2 = func2(7, 5)
print(r1, r2)
#so now the two return operation results will be printed seperately

def func3(x, y, z=None):
    print(x, y, z) #so the argument z will initially be unassigned and printed as 'None'

func3(10, 4)
func3(10, 4, 8) #z is now assigned and 'None' is overidden by '8'

def func(x):
    def func2():
        print(x)
    return func2

func(3)
#simply calling func wont do anything by definition
func(3)() 
#Now func is called with double brackets, it by definition calls func2 and so because func2 prints the argument x, x is printed

print(func(3)) #will print 3 (func -> func2)
print(func(3)()) #will then will print 'None' (func2)


##*ARGS **KWARGS##

x = [60, 30, 18, 48]
print(*x)
# the unpack operator * separates the list elements outputting them individually

def func(x, y):
    print(x, y)

pairs = [(1, 2), (3, 4)]
for pair in pairs:
    func(*pair)
# the unpack operator * will seperate the pair elements and output them as individual pairs

#alternatively in the case of dictionaries;   
    func(**{'x': 2, 'y': 5}) #x and y dont have to be in correct order as long as key matches argument

##so * is for unpacking lists, ** is for unpacking dictionaries

##say we have a function where we dont know how many arguments(pos or keyword) to accept
## *args and **kwargs allows us to pass in a unlimited amount of these arguments

def func(*args, **kwargs):
    print(args, kwargs)

func(1, 4, 5, 7, 2, 5, one=0, two=1)
#when we call the function, all pos arguments will be printed seperately (*args) as a tuple from all keyword arguments which will be printed seperately (**kwargs) as a set
#to actually print the unpacked the arguments individually, change the print statement to;
    print(*args)
#but this does not work with;
    print(**kwargs) #so the keyword arguments can be indivudally unpacked but not printed{error}

##SCOPES AND GLOBALS##

x = "apple"
#the above x variable and its assignment is global and limited to the scope of the file
def func(name):
    x = name
    #whereas the above x variable is limited only to the scope of the function, it is local to the function

print(x) #the global x assignment is printed
func("tomato")
print(x) #even though the function assigns x to the 'name' argument, the argument 'tomato' wont be printed because the function-independant assignment of x cannot be altered by the function
#hence 'apple' is still printed as a global
#you can access the global variable within the function but not change it within the function

def func(name):
    global x
    x = name

print(x)
func("tomato")
print(x)
#now the argument 'tomato' of the function is printed assigned to x for we have modified the global x variable by initiating the funcion local x as a "global" before assigning it to the argument

##EXCEPTIONS##

##examples of Exception functions
'''
raise Exception()
raise FileExistsError()
raise FloatingPointError()
#...
'''
#Handling Exceptions (try, except, finally)
try:
    x = 7 / 0
except ZeroDivisionError as e:
    print(e)
#in a typical case, the program would crash outputing a typical zero divion error but by raising the exception(zeroerrordivision) and printing the error message 'e' as an exception message, the program wont crash as it did and will output the error neatly
#we can alternatively just state the exception as Exception() as the program automatically recognizes the error as an exception and will still ouput the zero division error message

    x = 7 / 0
except Exception as e:
    print(e) #outputs neat zero division error message

#finally is used to complete the code no matter the exception if it has occured so finalizes the program in question
try:
    ...
except ...
finally:
    ...

##LAMBDA##

x = lambda x: x + 5
#lambda acts as a one-line anonymous function which when assigned to a variable(var = lambda), takes the variable(lambda var: ) and acts on it using the argument when calling the var
print(x(2))

x = lambda x, y: x + y
#now we have to argue two parameters, x and y
print(x(2, 4))

##MAP AND FILTER (TO INCLUDE USE OF LAMBDA)

x = [2, 5, 7, 11, 10, 36, 35, 100, 101]

'''
y = []
for i in x:
    y.append(i + 2)

print(x)
'''
#alternatively;
mapped = map(lambda i: i + 2, x)
#the map() function will act to mapp the result of the lambda function[i + 2 for i in x] to another list assigned 'mapped'
print(list(mapped))

filtered = filter(lambda i: i % 2 == 0, x) #lambda now acts as a bool function[due to ==] returning true or false[based on whether the operation returns a remainde(%) of 0 or not]
#the filter() function will act to filter the results of the lambda function[which now acts as a bool] in such that it will print the TRUE results
print(list(filtered))

filtered_false = filter(lambda i: i % 2 != 0, x)
#what was false before is now printed TRUE [!=]
print(list(filtered_false))

##f STRINGS##

#an f string [f''] will act to convert whatevery type input into the string into a string

x = 10
y = x + 8
z = True

print(f"Lefa loves the number {x}. He is {y} years old and that is {z}")
#x, y, z are all ouputed as a string





#COMPLETE!!#
