# link: https://leetcode.com/problems/majority-element
# Moore's Voting Algorithm

# time complexity O(N)
# space complexity O(1)
class Solution:
    def majorityElement(self, nums):
        el = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                el = nums[i]
                count = 1
            elif nums[i] == el:
                count += 1
            else:
                count -= 1

        # Verify the candidate
        c = 0
        for num in nums:
            if num == el:
                c += 1

        if c > len(nums) // 2:
            return el