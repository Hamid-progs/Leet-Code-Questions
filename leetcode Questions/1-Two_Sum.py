# link: https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i in range(len(nums)):
            rem = rem = target - nums[i]

            if rem in mp:
                return [i,mp[rem]]
            
            mp[nums[i]] = i
        