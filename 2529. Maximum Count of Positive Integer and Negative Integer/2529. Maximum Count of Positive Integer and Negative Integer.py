#
# Problem: 2529. Maximum Count of Positive Integer and Negative Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
# Language: python3
# Date: 2026-02-17


class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        def firstNeg(nums):
            
            left,right,ans=0,len(nums)-1,len(nums)
            while left<=right:
                mid=left+(right-left)//2

                if nums[mid]>=0:
                    ans=mid
                    right=mid-1

                else:
                    left=mid+1

            return ans


        def firstPos(nums):

            left,right,ans=0,len(nums)-1,len(nums)
            while left<=right:
                mid=left+(right-left)//2

                if nums[mid]>0:
                    ans=mid
                    right=mid-1

                else:
                    left=mid+1

            return ans


        #sol 4: O(logn) & O(1) space
        
        neg=firstNeg(nums)
        pos=len(nums)-firstPos(nums)

        return max(pos,neg)



        #sol 3: O(logn) time & O(1) sapce
        
        # return max(len(nums)-bisect_right(nums,0), bisect_left(nums, 0))
                
        left=bisect.bisect_left(nums,0)
        right=bisect.bisect_right(nums,0)

        pos=len(nums)-right
        zeros=right-left
        neg=left

        return max(pos,neg)

        

        #sol 2: O(n) time & O(1) space

        idx=bisect.bisect_right(nums,0)
        pos=len(nums)-idx
        zeros=nums.count(0)
        return max(pos, len(nums)-pos-zeros)



        #sol 1: O(n) time & O(1) space

        neg,pos=0,0
        for num in nums:
            neg+=num<0
            pos+=num>0

        return max(neg,pos)
