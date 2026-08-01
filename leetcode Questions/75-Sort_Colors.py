# link: https://leetcode.com/problems/sort-colors

# time complexity is O(N) 
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
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

        