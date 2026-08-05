# link: https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)

        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        if index == -1 :
            nums[:] = nums[::-1]
        else:
            for  i in range(n-1,index,-1):
                if nums[i] > nums[index]:
                    temp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = temp 
                    break

            nums[index+1:] = nums[index+1:][::-1]
            
