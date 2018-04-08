# Sharon Gibbons, 11-03-2018
# Project Euler Problem 5: Smallest multiple
# https://projecteuler.net/problem=5
# https://www.programiz.com/python-programming/examples/lcm

# Python program to find the least common multiple for a range of numbers

# defines function
def findlcm(x, y):

    # identifies numbers that are greater than and lesser than input integers
    if x > y:
       a, b = x, y          # a = greater number, b = lesser number
    else:
       a, b = y, x
    
    # checks if a division of the greater by lesser number is even
    r = a % b

    while r != 0:   # loop to execute if a division of the greater by lesser number is not even
        a, b = b, r
        r = a % b
    
    # gcd is common factor of input integers
    gcd = b

    # least common multiple is the computation of the product of the input integers divided by gcd
    # https://codility.com/media/train/10-Gcd.pdf
    lcm = int(int(x * y) / int(gcd))

    # output
    return lcm

# sets variables and keyword argument
l = range(1, 21)

x = l[0]
y = l[1]
lcm = findlcm(x, y)

# iterates called function over sequence
for i in range(1,20):
    lcm = findlcm(lcm, l[i])

# output
print(lcm)
