# Code always runs linearly
# First command will execute first, then second one and so on.
# We could use branching in the code to break this linearity

## We could ask questions with if, elif and else statements

# getting two values from input
inp1 = input('Enter first value: ')
inp2 = input('Enter second value: ')

# converting them to float
inp1 = float(inp1)
inp2 = float(inp2)

## NOW we ask question: we want to find the maximum of inp1 and inp2

if inp1 > inp2: 
    print('First value is bigger!')

if inp2 > inp1:
    print('Second value is bigger')

# you ask the question after if and then type a :
# then you need an indetion difference to write commands that are specific to if
# this program prints the bigger value
    
if inp1 > inp2:
    print(inp1)

if inp2 > inp1:
    print(inp2)

# This two ifs are independent, meaning that they will excecute regardless of the oucome of the other if
# you could also use else statement
    
if inp1 > inp2:
    print('First value is bigger: ' , inp1)

else:
    print('First value was not bigger!')

## Else will execute IF the condition in if statement was not true
    
# you could also use elif
    
if inp1 > inp2:
    print(inp1)

elif inp2 > inp1:
    print(inp2)

else:
    print('EQUAL')

# in this case, the elif statement will assess if the first condition is not true
    
    