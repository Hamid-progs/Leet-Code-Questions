# link: https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums, k):
        mp = {0:1}
        prefix_sum = 0
        count = 0


        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum-k in mp:
                count += mp[prefix_sum-k]
            
            mp[prefix_sum] = mp.get(prefix_sum,0) + 1
        
        return count
            

        
