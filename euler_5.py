# Sharon Gibbons, 12-03-2018
# Project Euler Problem 5: Smallest multiple
# https://projecteuler.net/problem=5
# https://www.programiz.com/python-programming/examples/lcm

# Python program to find the least common multiple for a range of numbers

# defines findgcd function (find greatest common factor/divisor)
    # https://codility.com/media/train/10-Gcd.pdf
def findgcd(x, y):
    if x % y == 0:  # if statement to identify 
        return y
    else:
        return findgcd(y, x % y)

# defines findlcm function (find least common multiple)
    # least common multiple is the computation of the product of the input integers divided by gcd of the input integers
    # https://codility.com/media/train/10-Gcd.pdf
def findlcm(x, y):
    lcm = int(int(x * y) // int(findgcd(x, y)))
    return lcm

# sets variables and keyword argument
l = range(1,21)

x = l[0]
y = l[1]
lcm = findlcm(x, y)

# iterates called function over sequence
for i in range(1,20):
    lcm = findlcm(lcm, l[i])

# output
print(lcm)
