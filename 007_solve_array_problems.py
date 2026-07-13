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

print(findLargest1(a))
