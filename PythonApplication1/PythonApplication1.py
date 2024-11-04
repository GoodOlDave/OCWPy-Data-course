from itertools import filterfalse
import math
import string
from symbol import return_stmt
from xml.dom.minidom import ElementInfo
def compare(x, y):
    if x>y:
        return 1
    if x==y:
        return 0
    else:
        return -1
def hypotenuse(l1,l2):
    return math.sqrt(l1**2+l2**2)
def is_between(x,y,z):
    if x<=y<=z:
        return True
    else:
        return False
def factorial(n):
    if not isinstance(n, int):
        print ('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print ('Factorial is not defined for negative integers.')
        return None
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
def ackermann(m,n):
    if m==0:
       return n + 1
    elif m>0 and n==0:
        return ackermann(m-1,1)   
    elif m>0 and n>0:
        return ackermann(m-1,ackermann(m,n-1))
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(word):
    l=len(word)
    if l<=1:
        return True
    if first(word)!=last(word):
        return False
    if first(word)==last(word):
        l-2
        return is_palindrome(middle(word))
def is_power(a,b):
    if a%b != 0:
        return ("a is not a power of b")
    if a/b==1:
        return("True")
    else:
       return is_power(a/b,b)
def gcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return gcd(b,r)
def print_n(s, n):
    while n>0:
        print(s)
        n=n-1
def square_root(a):
    x=3.0
    epsilon= 0.000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y
def comparesqrt(n):
    while n!=0:
        print (n,square_root(n),math.sqrt(n), abs(square_root(n)-math.sqrt(n))/n)
        n=n-1