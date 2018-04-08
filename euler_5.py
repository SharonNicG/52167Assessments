# Sharon Gibbons, 04-03-2018
# Project Euler Problem 5: Smallest multiple
# https://projecteuler.net/problem=5
# https://www.programiz.com/python-programming/examples/lcm

# Python Program to find the least common multiple for a range of numbers

# defines function
def findlcm(x, y):
    
    if x >= y:    # identifies number that greater than or equal to input integers
        greater = x
    else:
        greater = y

    # indefinite/infinite while loop evaluating the above conditional expression
    while(True):

       # checks if number is evenly divisible by input integers
        if((greater % x == 0) and (greater % y == 0)): 

           # if evenly divisible then the number is stored and the loop is broken
            lcm = greater
            break

        # if number if not evenly divisible number increments and loop continues
        greater = greater + 1

    # output
    return lcm

# sets variables and keyword argument
l = range(1, 21)
 
a = l[0]
b = l[1]
lcm = findlcm(a, b)

# iterates called function over sequence
for i in range(1,20):
    lcm = findlcm(lcm, l[i])

# output
print(lcm)
