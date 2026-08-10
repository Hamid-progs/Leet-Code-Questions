# link: https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    # time complexity O(nlogn)
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

    # time  complexity O(N)
    def longestConsecutive2(self, nums: List[int]) -> int:
        st = set(nums)
        if len(st) == 0 :
            return 0
            
        longest = 0

        for x in st:
            if x-1 not in st:
                cnt = 1
                while x+1 in st:
                    x += 1
                    cnt += 1

                longest = max(longest,cnt)

        return longest
        
