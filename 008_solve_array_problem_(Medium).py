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

# ----------------------------------------------------------

# Problem Statement: 
# Given an integer array nums of size n, return the majority element of the array.
# The majority element of an array is an element that appears more than n/2 times in the array. 
# The array is guaranteed to have a majority element.

# ---Solution 1---
# time complexity O(N) hashing approach
# space complexity O(N) hash map
def majority1(nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]):
    mp = {} 

    for i in range(len(nums)):
        if nums[i] not in mp:
            mp[nums[i]] = 1
        else:
            mp[nums[i]] += 1

        if len(nums)//2 < mp[nums[i]]:
            print(nums[i])
            break

# majority1()


# ---Solution 2---
# time complexity is O(N) or O(2N)
# space complexity is O(1) which is good
def majority2(nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]):
    el = nums[0]
    count = 1

    for i in range(1,len(nums)):
        if count == 0:
            el = nums[i]
            count = 1
        elif nums[i] == el:
            count += 1
        else:
            count -= 1

    # verify the canidate
    c = 0
    for i in range(len(nums)):
        if el == nums[i]:
            c += 1

    if c > len(nums)//2:
        print(el)
    else:
        print("NO majority element!")

# majority2()
