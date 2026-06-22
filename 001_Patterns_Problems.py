# 1. 
#  *****
#  *****
#  *****
#  *****
#  *****

def Q1():
    for i in range(1,6):
        for j in range(1,6):
            print("*",end = "")
        print()
# --------------------------------------

# 2. 
#  *
#  ** 
#  ***
#  ****
#  *****

def Q2():
    for i in range(1,6):
        for j in range(i):
            print("*",end="")
        print()
# --------------------------------------

# 3.
#  1
#  12 
#  123
#  1234
#  12345 

def Q3():
    for i in range (1,6):
        for j in range(i):
            print(j+1,end="")
        print()
# --------------------------------------

# 4. 
#  1
#  22 
#  333
#  4444
#  55555

def Q4():
    for i in range(1,6):
        for j in range(i):
            print(i,end="")
        print()
# -----------------------------------

# 5.
#  *****
#  ****
#  ***
#  **
#  *
def Q5():
    c=5
    for i in range(1,6):
        print("*"*c)
        c = c-1
# --------------------------------------
# 6. 
#  12345
#  1234
#  123
#  12
#  1
def Q6():
    c=6
    for i in range(1,6):
        for j in range(1,c):
            print(j,end="")
        c= c-1
        print()

# --------------------------------------
# 7.
#     *
#    ***
#   *****
#  *******
# *********
def Q7():
    c = 0
    o = 1
    for i in range(1,6):
        c = 5 - i 
        print(" "*c,"*"*o)
        o = o + 2
# -------------------------------------

# 8.
#  *********
#   *******
#    *****
#     ***
#      *

def Q8():
    c = 0
    o = 9
    for i in range(1,6):
        print(" "*c,"*"*o)
        c = c + 1
        o = o - 2
# -----------------------------------

9.
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def Q9():
    c = 0
    o = 1
    for i in range(1,6):
        c = 5 - i 
        print(" "*c,"*"*o)
        o = o + 2

    c = 0
    o = 9
    for i in range(1,6):
        print(" "*c,"*"*o)
        c = c + 1
        o = o - 2
# ----------------------------------

10.
#  *
#  ** 
#  ***
#  ****
#  *****
#  ****
#  ***
#  **
#  *

def Q10():
    for i in range(1,6):
        for j in range(i):
            print("*",end="")
        print()

    c=5
    for i in range(1,6):
        print("*"*c)
        c = c-1
# ------------------------------------

# 11.
#  1
#  01
#  101
#  0101
#  10101

def Q11():
    b = [1,0,1,1,0,1,0,1,0,1,1,0,1,0,1]
    c = 0
    for i in range(1,6):
        for j in range(i):
            print(b[c],end="")
            c = c + 1
        print()
# ------------------------------------

12.
#  1      1
#  12    21
#  123  321
#  12344321

def Q12():
    c = 6
    for i in range(1,5):
        for j in range(1,i+1):
            print(j,end='')
        print(" "*(c),end='')
        c = c-2
        for j in range(1,i+1):
            print(j,end='')
        print()
# ----------------------------------

# 13.
#  1
#  2 3
#  4 5 6
#  7 8 9 10
# 11 12 13 14 15

def Q13():
    c = 1
    for i in range(1,6):
        for j in range(1,i+1):
            print(c,end=" ")
            c = c+1
        print()
# ---------------------------------------

# 14.
#  A 
#  AB 
#  ABC 
#  ABCD 

# Logic for incrementing Alphabet in python
# a = "A"
# a=chr(ord(a) + 1)
# print(a)


def Q14():
    for i in range(1,5):
        a = "A"
        for j in range(1,i+1):
            print(a,end="")
            a = chr(ord(a) + 1)
        print()

# it will prints ascii value of character
# print(ord('B')) 
# -------------------------------------------

# 15.
#  ABCDE
#  ABCD
#  ABC
#  AB 
#  A

def Q15():
    for i in range(1,6):
        a = 'A'
        for j in range(1,7-i):
            print(a,end='')
            a = chr(ord(a) + 1)
        print()

# ---------------------------------------

# 16.
#  A 
#  BB 
#  CCC 
#  DDDD
#  EEEEE

def Q16(): 
    a = 'A'
    for i in range(1,6):
        for j in range(1,i+1):
            print(a,end='')
        print()
        a = chr(ord(a) + 1)

# ----------------------------------

# 17.
#     A
#    ABA
#   ABCBA
#  ABCDCBA

def Q17():
    for i in range(1,5): 
        a = 'A'
        point = i - 2
        lst = []
        print(' '*(4-i),end='')
        for j in range(1,i+1):
            print(a,end='')
            lst.append(a)
            a = chr(ord(a) + 1)
            l = len(lst)
        if l != 1:
            lst = lst[0:point+1]
            for ls in lst[::-1]:
                print(ls,end='')
        print()
# --------------------------------------

# 18.
#  E 
#  D E 
#  C D E 
#  B C D E
#  A B C D E 

def Q18():
    o = 'E'
    for i in range(1,6):
        a = o
        for j in range(1,i+1):
            print(a,end=' ')
            a = chr(ord(a) + 1)
        print()
        o = chr(ord(o) - 1)
# -----------------------------------------

# 19. 
#  **********
#  ****  ****
#  ***    ***
#  **      ** 
#  *        *
#  **      **
#  ***    ***
#  ****  ****
#  **********

def Q19():
    c=5
    d=0
    for i in range(1,6):
        print("*"*c,end='')
        if d != 0:
            print(" "*d,end='')
        print("*"*(6-i))
        d = d+2
        c = c-1

    d = 6
    for i in range(1,6):
        if i != 1:
            print("*"*i,end='')
            if d != 0:
                print(" "*d,end='') 
            print("*"*i)
            d = d-2
