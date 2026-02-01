#
# Problem: 1877. Minimize Maximum Pair Sum in Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/submissions/1904575591/?envType=problem-list-v2&envId=waksgnnd
# Language: python3
# Date: 2026-02-01


class Solution:
    def minPairSum(self, nums: List[int]) -> int:

      #sol 2: O(nlogn) time & O(n) space

      return (lambda lst: max(lst[i]+lst[~i] for i in range(len(lst)//2))) (sorted(nums))      



      #sol 1: O(nlogn) time & O(1) space

      nums.sort()

      i,j=0,len(nums)-1
      maxVal=float('-inf')

      while i<=j:
        maxVal=max(maxVal,nums[i]+nums[j])

        i+=1
        j-=1
      
      return maxVal
        
