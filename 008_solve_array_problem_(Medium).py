# Problem Statement: Given an array of integers arr[] and an integer target.
# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

# ---Solution 1---
# time complexity O(N)
def check_pair1(a = [2,6,5,8,11],k=14):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] + a[j] == k :
                print('yes')
                print("i:",i,"\nj:",j)
                break
        if a[i] + a[j] == k :
            break

# check_pair1()

# ---Solution 2---
# time complexity O(N)
def check_pair2(a = [2,6,5,8,11],k=15):
    mp = {}
    for i in range(len(a)):

        rem = k - a[i]

        if rem in mp:
            print('yes')
            print(mp[rem],i)
            return True

        mp[a[i]] = i
        
    print('No')
    return False
    


# check_pair2()

# ---Solution 3---
# only when the array is sorted
# Time complexity O(N)  best optial solution
def check_pair3(a = [2,4,6,8,11],k=15):
    left = 0
    right = len(a)-1

    while left < right:
        sum = a[left] + a[right]
        
        if sum == k:
            print('yes')
            print('index: ',left,',',right)
            return True
        elif sum < k:
            left +=1
        else:
            right -= 1

    print("NO!")
    return False


# check_pair3()

# ------------------------------------------------------

# Problem Statement: 
# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
# The sorting must be done in-place, without making a copy of the original array.

# ---Solution 1---
# time complexity O(NlogN)
def sort_array1(nums = [1, 0, 2, 1, 0]):
    nums.sort()
    print(nums)

nums = [1, 0, 2, 1, 1]
# sort_array1(nums)

# ---Solution 2---
# time complexity O(N) best solution
def sort_array2(nums = [0, 0, 1,1,1,2,1,2,0,0,0]):
    mid = 0
    low = 0
    high = len(nums)-1

    while mid <= high:
        if nums[mid] == 0:
            temp = nums[low]
            nums[low] = nums[mid]
            nums[mid] = temp
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            temp = nums[high]
            nums[high] = nums[mid]
            nums[mid] = temp
            high -= 1
    print(nums)

# sort_array2()

