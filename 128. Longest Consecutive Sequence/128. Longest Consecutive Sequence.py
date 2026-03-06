#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Language: python3
# Date: 2026-03-06


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #sol 1: O(nlogn) time & O(n) space

        if not nums:
            return 0

        uni=list(set(nums))
        uni.sort()

        ctr,maxVal=1,1
        for i in range(len(uni)-1):
            if uni[i+1]-uni[i]==1:
                ctr+=1
            else:
                maxVal=max(maxVal,ctr)
                ctr=1

        maxVal=max(maxVal,ctr) #must update if there's no a gap, reached the end-> don't return ctr but update hte maxVal
        return maxVal
