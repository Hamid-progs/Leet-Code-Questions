# link: https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums, k) :
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[-k:] + nums[:-k]