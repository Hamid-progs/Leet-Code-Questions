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

# --------------------------------------------------------------

# Problem Statement: 
# Given an integer array nums,
# find the subarray with the largest sum and 
# return the sum of the elements present in that subarray.

# time complexity O(N) best solution
def max_sum_subarray(nums = [-5,4,6]):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1,len(nums)):
        current_sum = max(nums[i],current_sum+nums[i])
        max_sum = max(max_sum,current_sum)
    print(max_sum)

# max_sum_subarray()

# ----------------------------------------------------------------------------------------------------------------------

# Problem Statement:
# You are given an array of prices where prices[i]
# is the price of a given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock. 
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# time complexity is O(N)
def stock_profits(prices = [7,6,4,3,1]):
    min_price = prices[0]
    max_profit = 0 

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit,price-min_price)
        
    print(max_profit)

# stock_profits()

# ------------------------------------------------------------

# Problem Statement: There’s an array ‘A’ of size ‘N’ with 
# an equal number of positive and negative elements. Without altering
#  the relative order of positive and negative elements,
# you must return an array of alternately positive and negative values.

# ---Solution 1---
# time complexity O(N) + O(N)  or O(N)
# space complexity O(N)
def pos_neg_element1(a = [1,2,-3,-1,-2,3]):
    pos = []
    neg = []
    for i in range(len(a)):
        if a[i] >= 0:
            pos.append(a[i])
        else:
            neg.append(a[i])

    for i in range(len(a)//2):
        a[2*i] = pos[i]
        a[(2*i)+1] = neg[i]

    print(a)

pos_neg_element1()

# ---Solution 2---
# time complexity O(N)
# space complexity O(N)
def pos_neg_element2(a = [1,2,-3,-1,-2,3]):
    n = len(a)
    ans = [0]*n
    pos = 0
    neg = 1

    for i in range(len(a)):
        if a[i] < 0:
            ans[neg] = a[i]
            neg += 2
        else:
            ans[pos] = a[i]
            pos += 2
    print(ans)

# pos_neg_element2()

# ------------------------------------------------------------

# Problem Statement: Given an array Arr[] of integers, 
# rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange to the lowest possible order
# (i.e., sorted in ascending order).

# time complexity O(N) or O(2N)
def next_permutation(a = [3,2,1]):
    index = -1
    n = len(a)

    for i in range(n-2,-1,-1):
        if a[i] < a[i+1]:
            index = i
            break

    if index == -1 :
        a = a[::-1]
        return a 

    for  i in range(n-1,index,-1):
        if a[i] > a[index]:
            temp = a[i]
            a[i] = a[index]
            a[index] = temp 
            break

    a[index+1:] = a[index+1:][::-1]
    return a

# print(next_permutation())

# -------------------------------------------------------------------------------------------------------

# Problem :
# select leaders from the given element 
# leaders is the element whose right side contain small elements

# ---Solution 1---
# time complexity O(N^2)
# space complexity O(N) for storing the result
def leaders1(a = [10,22,12,3,0,6]):
    leaders = []

    for i in range(len(a)):
        l = a[i]
        for j in range(i+1,len(a)):
            if i == len(a)-1:
                leaders.apped(l)

            if l < a[j]:
                l=-1
                break
            
        if l != -1:
            leaders.append(l)

    print(leaders)

# leaders1()

# ---Soulution 2---
# time complexity O(N)
# space complexity O(N) because we are storng the results
def leaders2(a = [10,22,12,3,0,6]):
    max_el = a[-1]
    leaders = []
    leaders.append(max_el)
    for i in range(len(a)-2,-1,-1):
        if a[i] > max_el:
            max_el = a[i]
            leaders.append(max_el)

    # the result is in right to left fashion
    print(leaders)
    # if you want left to right fashion reverse the list
    # print(leaders[::-1])

# leaders2()

# -----------------------------------------------------------------------------------

# Problem Statement: 
# Given an array nums of n integers.
# Return the length of the longest sequence of consecutive integers. 
# The integers in this sequence can appear in any order.

# time complexity O(nlogn)
# space complexity O(n)
def max_consecutive_sequence(nums = [100, 4, 200, 1, 3, 2]):
    nums.sort()
    print(nums)
    el = nums[0]
    max_l = 1
    l = 1
    for i in range(1,len(nums)):
        if nums[i] == el:
            continue
        
        if nums[i] == el + 1:
            l += 1
        else:
            max_l = max(max_l,l)
            l = 1

        el = nums[i]

    max_l = max(max_l,l)
            


    print(max_l)

# max_consecutive_sequence()

