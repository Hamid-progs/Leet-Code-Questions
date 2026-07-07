# merge sort
# time complexity O(log2(n))
def merge_sort(a, low, high):
    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(a, low, mid)
    merge_sort(a, mid + 1, high)

    merge(a, low, mid, high)


# merging code
def merge(a, low, mid, high):
    temp = []

    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if a[left] <= a[right]:
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
        right += 1

    # Copy the merged elements back into the original array
    for i in range(low, high + 1):
        a[i] = temp[i - low]


# Driver code
a = [3, 1, 2, 4, 1, 5, 2, 6, 4]

merge_sort(a, 0, len(a) - 1)

print(a)