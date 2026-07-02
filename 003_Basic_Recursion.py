"""
Q: What is Recursion?
Ans: When a function call itself 
until a specific condition is met
"""

# ----------------------------------------

# Understand recursion by print something N times

count = 0 
def f(n):
    global count  # it says that this is a global variable count
    if count == n :
        return 
    else:
        print(count)
        count = count + 1
        f(n)

        # this will tell the function is terminated 
        # and send out of stack (LIFO) Last in first out
        count -= 1
        # example of LIFO:
        print(f'function {count} terminated!')
        
# f(11) 


# if condition = 3
# ===============Recursion Tree==========================
                    #       f()
                    #      / ^
# moving down       #     f()|     
                    #    /  ^    moving up back to previous
                    #   f() |     function
                    #  /  ^   
                    # f() |  
# ========================================================


# -----------------------------------------------------

# print Name N time using Recursion 

def N_name(n,name):
    if n == 0:
        return 
    else:
        print(name)
        n -= 1
        N_name(n,name)

# this will print name ,'n' times
# N_name(10,"Hamid")


# -------------------------------------------------------

# print 1-N using recursion 
count = 1
def print1_N(n):
    global count
    if count > n:
        return
    else:
        print(count) 
        count += 1 
        print1_N(n)

# print1_N(11)
# --------------------------------------------------------------------

# Print N to 1 using Recursion

def printN_1(n):
    count = n 
    if count == 0:
        return 
    else:
        print(count)
        count -= 1
        printN_1(count)

# printN_1(11) 

# ------------------------------------------------------------------

# Sum of First N Numbers

sum = 0
count = 1
def sum_N1(n):
    global sum
    global count 

    if count > n:
        print(f"Sum : {sum}")
        return 
    else:
        sum += count 
        count +=1 

        sum_N1(n)
        

# sum_N1(4)

# parmetrized way 

def sum_N2(i,sum):
    if (i < 1):
        print(f"Sum : {sum}")
        return
    sum_N2(i-1,sum+i)

# sum_N2(3,0)

# function way 

def sum_N3(n):
    if (n == 0):
        return 0
    return n + sum_N3(n-1)

# print(sum_N3(4))

# -------------------------------------------

# Factorial of a given number

# time complexity O(n)
# Space complexity O(n)
# usnig fucntion method: 
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# print(factorial(5))

# ---------------------------------------

# reverse an array 

# with out using recursion or loops
def reverse1(l):
    return l[::-1]

# print(reverse([1,2,3,4,5,6]))

# 1. using recursion by swaping  

def reverse2(l,head,tail):
    if head >= tail:
        return l
    else:
        temp = l[head]
        l[head] = l[tail]
        l[tail] =temp

        return reverse2(l,head+1,tail-1)

# li = [1,2,3,5,2]
# print(reverse2(li,0,len(li)-1))

# 2. reverse using one pointer 

def reverse3(l,head=0):
    length = len(l)
    if head >= length // 2:
        return l 
    else:
        temp = l[head]
        l[head] = l[length-head-1]
        l[length-head-1] = temp

        return reverse3(l,head+1)

# print(reverse3([1,2,3,5,2]))

# ---------------------------------------------------

# palandrome the string  array 
def palindrome_string(original, new=None, head=0):
    if new is None:
        new = original.copy()

    length = len(new)

    if head >= length // 2:
        if original == new:
            return f"{original} is Palindrome"
        else:
            return f"{original} is not Palindrome"
    
    temp = new[head]
    new[head] = new[length-head-1] 
    new[length-head-1] = temp

    return palindrome_string(original, new, head+1)

# print(palindrome_string(['a','b','c','a']))
# print(palindrome_string(['a','b','a']))

# leet code Question check the string is palandrorm or not:
# this question is not solved by recursion
import re

def isPalindrome( s):
    s =  re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    if s == s[::-1]:
        return True
    return False 
    
# by recursion method
def p(s,c=1):
    if c == 1:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        c = c-1
    if len(s) <= 1:
        return True 
    if s[0] != s[-1]:
        return False 
    return p(s[1:-1],c)

s = "A man, a plan, a canal: Panama"
# print(p(s))

# ----------------------------------------------------------

# fibonacci Numbers

def fibonacci(n):
    if n <= 1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(8))

# --------------------------------------------------------

