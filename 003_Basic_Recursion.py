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



