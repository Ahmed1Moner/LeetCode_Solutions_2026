#
# Problem: 2966. Divide Array Into Arrays With Max Difference
# Difficulty: Medium
# Link: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/submissions/1897739537/?envType=problem-list-v2&envId=w95808hv
# Language: python3
# Date: 2026-01-26


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        #sol 1: greedy -> O(nlogn) time & O(1) space

        nums.sort()
        ans=[]

        for i in range(0,len(nums),3):
            if nums[i+2]-nums[i]>k:
                return []
            
            ans.append([nums[i],nums[i+1],nums[i+2]])
        
        return ans
