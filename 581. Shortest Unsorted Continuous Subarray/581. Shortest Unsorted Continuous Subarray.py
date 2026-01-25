#
# Problem: 581. Shortest Unsorted Continuous Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Language: python3
# Date: 2026-01-25


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        #Sol 4: O(n) time O(1) space
        left,right=-1,-1

        maxVal=float('-inf')
        for i in range(len(nums)):
            if nums[i]<maxVal:
                right=i
            else:
                maxVal=nums[i]

        minVal=float('inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>minVal:
                left=i
            else:
                minVal=nums[i]
        
        return right-left+1 if left!=-1 else 0




        # #Sol 3: O(n) time & O(n) space
        # n=len(nums)
        # minlst,maxlst=[0]*n,[0]*n

        # maxVal=nums[0]
        # for i in range(n):
        #     maxVal=max(maxVal,nums[i])
        #     maxlst[i]=maxVal
        
        # minVal=nums[-1]
        # for i in range(n-1,-1,-1):
        #     minVal=min(minVal,nums[i])
        #     minlst[i]=minVal
        
        # left,right=0,n-1

        # while left<n and nums[left]==minlst[left]==maxlst[left]:
        #     left+=1
        
        # while right>=0 and nums[right]==minlst[right]==maxlst[right]:
        #     right-=1
        
        # return right-left+1 if left<=right else 0



        # #Sol 2: O(nlogn)
        # target=sorted(nums)
        # if nums==target:
        #     return 0

        # left,right=0,len(nums)-1

        # while left<=right:
        #     if nums[left]==target[left]:
        #         left+=1
        #     elif nums[right]==target[right]:
        #         right-=1
        #     else:
        #         break
        
        # return right-left+1




        # #Sol 1: O(n^3logn) TLE Brute Force
        
        # target=sorted(nums)
        # #base case
        # if nums==target:
        #     return 0
        
        # minVal=len(nums)
        # for left in range(len(nums)):
        #     for right in range(left,len(nums)):

        #         if target == (nums[:left] + sorted(nums[left:right+1]) + nums[right+1:]):
        #             minVal=min(minVal, right-left+1)
        
        # return minVal
