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





