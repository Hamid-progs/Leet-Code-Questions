# Merge Sort :
# time complexity o(log2(n))

a = [3, 1, 2, 4, 1, 5, 2, 6, 4]

def MergeSort(a,low,high):
    if  low >= high:
        return 

    mid = (low + high) // 2

    MergeSort(a,low,mid)
    MergeSort(a,mid+1,high)
    Merge(a,low,mid,high )


def Merge(a,low ,mid ,high):
    temp = []

    left = low 
    right = mid+1

    while left <= mid and right <=high:
        if a[left] < a[right]:
            temp.append(a[left])
            left += 1
        else:
            temp.append(a[right])
            right += 1
    
    while left <= mid:
        temp.append(a[left])
        left += 1
    
    while right <= high:
        temp.append(a[right])
        right +=1
    
    for i in range(low,high+1):
        a[i] = temp[i-low]






# Driver code
# a = [3, 1, 2, 4, 1, 5, 2, 6, 4]
# MergeSort(a, 0, len(a) - 1)
# print(a)

# =============================================

# Bubble sort by recursion 

a = [3, 1, 2, 4, 1, 5, 2, 6, 4]
def BubbleSort(a,n= None):
    if n is None:
        n = len(a)
    
    # base case
    if n == 1:
        return

    swap = False
    for i in range(n-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1]= temp
            swap = True
    
    if not swap :
        return
    
    BubbleSort(a,n-1)

# BubbleSort(a,)
# print(a)

# ============================================================

# insertion sort by recursion 
def InsertionSort(a , i=1):

    if i >= len(a):
        return

    j = i
    while j > 0 and a[j-1] > a[j]:
        temp = a[j-1]
        a[j-1] = a[j]
        a[j] = temp 
        j = j-1

    InsertionSort(a , i+1)

# a = [3, 1, 2, 4, 1, 5, 2, 6, 4]
# InsertionSort(a)
# print(a)

# =================================================

# Quick Sort 

def QuickSort(a,low,high):
    if low < high:
        partition_index = Helping_function(a,low,high)
        QuickSort(a,low,partition_index-1)
        QuickSort(a,partition_index+1,high)

def Helping_function(a,low,high):
    pivot = low
    i = low 
    j = high 

    while i < j:
        while a[i] <= a[pivot] and i <=high-1:
            i += 1
        while a[j] >= a[pivot] and j >=low+1:
            j -= 1
        if i < j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp 
    # this will take pivot to its position
    temp = a[pivot]
    a[pivot] = a[j]
    a[j] = temp

    return j 

a = [3, 1, 2, 4, 1, 5, 2, 6, 4]

# print(a)
# QuickSort(a,0,len(a)-1)
# print(a)

# =================================================

