# Sharon Gibbons, 10-02-2018
# The Collatz Conjecture programme
# https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please input an integer value: "))

while n != 1:                   # check for infinite while loop
    if n % 2 == 0:              # if integer value is even
        n = (int(n // 2))
    else:                       # if integer value is odd
        n % 2 == 1
        n = (int(3 * n + 1))
    print(n)                    # print Collatz Conjecture sequence for inputed value
