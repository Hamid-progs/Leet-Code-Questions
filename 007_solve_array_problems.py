# Statement: Given an array, we have to find the largest element in the array.

# solution 1:
# time complexity O(N)  # best solution
def findLargest(a):
    max = a[0]
    for i in a:
        if i > max:
            max = i
        
    return max

a = [8, 10, 5, 7, 9]
print(findLargest(a))

# solution 2:
# time complexity O(N)  # best solution
print(max(a))

# solution 3: 
# time complexity O(Nlog(N)) 
def findLargest1(a):
    a.sort()   
    return a[-1]

# print(findLargest1(a))

# -------------------------------------------------------

# Find Second Smallest and Second Largest Element in an array

# ---solution 1:---
# time complexity is O(Nlog(N))
def second_smallest_largest1(a = [8, 10, 5, 7,9, 9]):
    a.sort()
    
    if len(a) == 1:
        print(f'Second Smallest: {a[0]}')
        print(f'Second Largest : {a[0]}')
    else:
        print(f'Second Smallest: {a[0]}')
        print(f'Second Largest : {a[-1]}')


# second_smallest_largest1()

# ---solution 2:---
# best case O(1)  if array lenght == 1
# worst case O(2N)
def second_smallest_largest2(a = [8, 10, 5, 7,10, 9]):

    if len(a) == 1:
        print(-1)     # means nothing second largest nothing = -1
        print(a[0])
        return
    
    a.sort()

    mx = a[-1]  # max
    mi = a[0]   # min

    for i in a[::-1]:
        if i < mx:
            print(i)
            break
    
    for i in a:
        if i > mi:
            print(i)
            break
        
# second_smallest_largest2()

# -----------------------------------------------------
# Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

# ---Solution 1:---
# time Complexity O(N)
def check_array_is_sorted(a = [8, 10, 5, 7,10, 9]):
    for i in range(0,len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

# print(check_array_is_sorted())

# --------------------------------------------------------

# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

# ---Solution1: ----
# time complexity O(N)
def remove_duplicates1(a = [1,1,2,2,2,3,3]):
    a = set(a)
    print(a)
    
# remove_duplicates()

# ---Solution2---
# time complexity O(N)
def remove_duplicates2(a = [1,1,2,2,2,3,3]):
    a.append(None)

    b = list()

    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            b.append(a[i])
    print(b)

# remove_duplicates2()

# -------------------------------------------------------------

# Problem Statement: Given an integer array nums, rotate the array to the left by one.

# ---Solution1:---
# time complexity O(k x N) where k is number of roataions
def rotate_array1(nums = [1, 2, 3, 4, 5], rotation = 1):

    for i in range(0,rotation):
        temp = nums[0]
        for j in range(1,len(nums)):
            nums[j-1] = nums[j]
        nums[len(nums)-1] = temp

# nums = [1, 2, 3, 4, 5]
# rotate_array1(nums)
# print(nums)

# ---Solution2:---
# time complexity is O(N)  optimal solution
def rotate_array2(nums = [1, 2, 3, 4, 5],rotation = 1):
    nums[:] = nums[rotation:] + nums[:rotation]
    # nums[:] doesn't create a new list variable. Instead, 
    # it replaces all the elements inside the existing list.


# nums = [1, 2, 3, 4, 5]
# rotate_array2(nums)
# print(nums)

# ---------------------------------------------------------
# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

# ---Solution1:---
# time complexity is O(N)  optimal solution
def rotate_array(nums,rotation,direction):
    r = rotation % len(nums)

    if direction == 'left' or direction == -1:
        nums[:] =  nums[r:] + nums[:r]
    elif direction == 'right' or direction == 1:
        nums[:] = nums[-r:] + nums[:-r]
    else:
        raise ValueError("Direction must be 'left', 'right', -1, or 1")

# use:
#   rotation = 'left' or -1
#   rotation = 'right' or 1

# nums = [1, 2, 3, 4, 5]
# rotate_array(nums,2,'left')
# print(nums)

# nums = [1, 2, 3, 4, 5]
# rotate_array(nums,2,'right')
# print(nums)

# ------------------------------------------------------------------------

# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

# ---Solution1---
# time complexity O(N^2)
def move_zeros1(a = [1,0,2,3,0,4,0,1]):
    n = len(a)
    i = 0
    while i < n:
        if a[i] == 0:
            temp = a[i]
            for j in range(i,n-1):
                a[j] = a[j+1]
            a[n-1] = temp
            n -= 1
        else:
            i += 1
    print(a)

# move_zeros1()


# ---Solution2---
# time complexity O(N)   optimal solution
def move_zeros2(a = [1,0,2,3,0,0,4,0,1]):
    left = 0 

    for right in range(len(a)):
        if a[right] != 0:
            # swap
            temp = a[left]
            a[left] = a[right]
            a[right] = temp

            left += 1
    print(a)

# move_zeros2()

# -------------------------------------------------------------------

# Problem Statement: Given an array, 
# and an element num the task is to find if num is present in the given array or not. 
# If present print the index of the element or print -1.

# ---Solution 1---
# time complexity O(n) worst case , O(1) best case if element at first
def linear_check1(a = [1,2,3,4,5] ):
    print(a[3])
    check = int(input("Enter a Number to check : "))

    for i in range(len(a)):
        if check == a[i]:
            print(f'index: {i}')
            check = 0

    if check != 0:
        print(-1)


# --- Solution 2---
# for creating the dictionary the time complexity will be O(N)
# searching in dictionary is O(1) 

# if you want mulitiple search the fist attempt will be O(N)
# because of dictionary formation , the extracting value from 
# dictionary will be O(1)

def linear_check2(a = [1,2,3,4,5] ):
    # time complexity is O(N)
    mapp_ind = dict()
    for i in range(len(a)):
        mapp_ind[a[i]] = i

    # time complexity O(1)
    check = int(input("Enter a number: "))
    print(mapp_ind.get(check,-1))

# linear_check1()
# linear_check2()

# --------------------------------------------------------------

# Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
# The union of two arrays can be defined as the common and distinct elements in the two arrays.
# NOTE: Elements in the union should be in ascending order.

# --- Solution 1---
# time complexity is O(N x k)
def union1(a1 = [1,2,3,4,5],a2 = [2,3,4,4,5]):
    uni = []

    if len(a1) > len(a2):
        min_a = a2   # min lenght
        max_a = a1   # max length
    else:
        min_a = a1   # min lenght
        max_a = a2   # max lenght
        
    for i in range(len(min_a)):
        for j in range(len(max_a)):
            if min_a[i] == max_a[j]:
                uni.append(min_a[i])
                break  
    print(uni)

# union1()
    
