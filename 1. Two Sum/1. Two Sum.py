#
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/description/
# Language: python3
# Date: 2026-02-23


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #sol 4: O(n) time & O(n) space

        mapp={}
        for i in range(len(nums)):
            temp=target-nums[i]
            
            if temp in mapp:
                return [i,mapp[temp]]
            
            mapp[nums[i]]=i


        #sol 3: O(n^2) time & O(n) space

        mapp=set(nums)

        for i in range(len(nums)):
            mapp.remove(nums[i])

            temp=target-nums[i]
            if temp in mapp:
                return [nums.index(nums[i]),nums.index(temp)]
            
            mapp.add(nums[i])



        #sol 2: O(n^2) time & O(1) space

        for i in range(len(nums)):
            temp=target-nums[i]
            j=i+1

            while j<len(nums):
                if temp-nums[j]==0:
                    return [i,j]
                j+=1
        
        return -1


        #sol 1: O(n^2) time & O(1) space

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

        return -1
