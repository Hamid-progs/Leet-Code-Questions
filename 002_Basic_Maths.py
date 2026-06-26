import math

# --------------------------Concept1----------------------------
# Count All digit of a Number  

# input = 12345
# output = 5

def CountDigit1(n):
    c = 0
    while(n>0):
        """
            this truncate the decimal 
            point mean in each 
            iteration remove the decimal point

            example first iteration:
            7789 / 10 = 778.9
            int(778.9) = 778

            hence 9 is removed and new number is 778

            Time Complexity = O( log10(n) )

        """
        n = int(n / 10)
        c = c+1
    print(c) 


def CountDigit2(n):

    """
        log10(7789) = 3.89
        3.89 + 1 = 4.89
        int(4.89) = 4 
        
        4 which is the count of 7789

    """

    c = int(math.log10(n)+1)
    print(c)

# ----------------------Concept2---------------------

# Reverse Integers

# LeetCode Question 7. Reverse Integers https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer
# range [-2^31, 2^31 - 1], then return 0.
# Input: x = 123
# Output: 321


def reverse(x):
    reverse = 0
    if x>0 :
        while(x>0):
            current = x % 10
            x = int(x / 10)
            reverse = (reverse * 10) + current
    else:
        x = abs(x)
        while(x>0):
            current = x % 10
            x = int(x / 10)
            reverse = ((reverse * 10) + current)
        reverse = reverse * -1
            
    if reverse > 2 ** 31 - 1 or reverse < -2 ** 31:
        print(0)
        return 0

    print(reverse)
    return reverse

# ----------------------------------------------------------