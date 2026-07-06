# Selcetion Sort
# time complexity for average and worst and good case is o(n^2)
def SelectionSort(l = [13,46,24,52,20,9]):
    for  i in range(0,len(l)-1):
        mini = i 
        for j  in range(i,len(l)):
            if l[j] < l[mini]:
                mini = j
                temp = l[mini]
                l[mini] = l[i]
                l[i] = temp
    print(l)

# SelectionSort()

# ---------------------------------------------------

# Bubble sort 

# time complexity for average and worst case is o(n^2)
def BubbleSort(l = [13,46,24,52,20,9]):
    didswap = 0  # this will be an indicatior if it remain zero no swaping occur hence array is sorted time compelxity o(n)
    for i in range(1,len(l)):
        for j in range(0,len(l)-i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                didswap = 1

        if didswap == 0:
            break    
        
    print(l)

# BubbleSort()

# ---------------------------------------------------

# Bubble sort 

# time complexity for average and worst case is o(n^2)
def BubbleSort(l = [13,46,24,52,20,9]):
    didswap = 0  # this will be an indicatior if it remain zero no swaping occur hence array is sorted time compelxity o(n)
    for i in range(1,len(l)):
        for j in range(0,len(l)-i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                didswap = 1

        if didswap == 0:
            break    
        
    print(l)

# BubbleSort()
