####################################  OUTPUT ####################################
# we output things using print command]
print('Hello World!')

# You can print values or/and variebles
print(1)        # print integer
print(3.14)     # print float
print('Hello')  # print string

# You can also print variables

v1 = 'Hello'
print(v1)

v2 = 12
print(v2)

v3 = 2.718
print(v3)

## You can also trail multiple things in the print function
print('Hello World!' , 12 , 9.8 , v1 , v2)
## you need a comma , between items in print function.


####################################  INOPUT ####################################

## To get input from the user you need 'input()' command

inp = input("Enter Something: ")
print(inp)

# Anything that you have wrote in the parantheses will be printed to the output first

inp = input() # dosent write anythin in the console and it just waits for the input
print(inp)

# input() returns a ::string:: (or str)
inp1 = input('Enter Value 1:')
inp2 = input('Enter Value 2:')

print(inp1 + inp2)
## + Operator, just connects to inputs together

## In order to use mathmatical operation on NUMERICAL inputs you need to convert str to float or int
## it is done using float() or/and int()

inp_int = int( input('Enter integer value:') )
inp_float = float( input('Enter float value:') )
print(inp_int , inp_float , inp_float + inp_int)
# this now ADDS the inputs numericaly together

