# Sharon Gibbons, 04-02-2018
# A program that displays Fibonacci numbers using people's names.
# https://github.com/ianmcloughlin/python-fib/blob/master/fib.py
# https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Gibbons"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
