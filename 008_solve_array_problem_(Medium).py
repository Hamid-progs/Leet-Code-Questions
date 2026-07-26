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


check_pair3()