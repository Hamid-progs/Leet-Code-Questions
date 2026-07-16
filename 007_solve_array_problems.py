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
