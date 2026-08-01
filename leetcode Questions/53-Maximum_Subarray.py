# link: https://leetcode.com/problems/maximum-subarray

# time complexity is O(n-1)
class Solution:
    def maxSubArray(self, nums):
        c = nums[0]
        m = nums[0]

        for i in range(1,len(nums)):
            c = max(nums[i],c+nums[i])
            m = max(m,c)
        return m
        