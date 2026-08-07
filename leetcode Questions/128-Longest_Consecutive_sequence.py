# link: https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums):
        if nums == []:
            return 0

        nums.sort()
        el = nums[0]
        max_l = 1
        l = 1

        for i in range(1,len(nums)):
            if nums[i] == el:
                continue 
            
            if nums[i] == el+1:
                l += 1
            else:
                max_l = max(max_l,l)
                l=1
            el = nums[i]

        max_l = max(max_l,l)
        return max_l

        