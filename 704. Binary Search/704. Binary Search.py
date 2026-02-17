#
# Problem: 704. Binary Search
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-search/submissions/1922095842/
# Language: python3
# Date: 2026-02-17


class Solution:
    def helper(self,nums,target,left,right):
        
        if left<=right:
            mid=(left+right)//2

            #base case
            if nums[mid]==target:
                return mid
            
            elif nums[mid]<target:
                return self.helper(nums,target,mid+1,right)
            
            else:
                return self.helper(nums,target,left,mid-1)
        
        else:
            return -1
            

    def search(self, nums: List[int], target: int) -> int:

        #sol 3: O(logn) time & O(1) sapce
        
        if target in nums:
            return bisect.bisect_left(nums,target)
        
        return -1


        
        #Sol 2: O(logn) time & O(logn) space
        
        return self.helper(nums,target,0,len(nums)-1)
        

        
        #Sol 1: O(logn) time & O(1) space

        #quick skip
        if target<nums[0] or target>nums[-1]:
            return -1

        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2

            #base case
            if nums[mid]==target:
                return mid
            
            elif nums[mid]<target:
                left=mid+1
            
            elif nums[mid]>target:
                right=mid-1


        return -1
