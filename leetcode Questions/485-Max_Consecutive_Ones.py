# link: https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                if max_count < c:
                    max_count = c
                c = 0

        if max_count < c:
            max_count = c
        
        return max_count
        