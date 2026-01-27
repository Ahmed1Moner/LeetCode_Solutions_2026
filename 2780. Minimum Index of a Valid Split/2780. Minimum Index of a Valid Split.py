#
# Problem: 2780. Minimum Index of a Valid Split
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-index-of-a-valid-split/?envType=problem-list-v2&envId=w95808hv
# Language: python3
# Date: 2026-01-27


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        #O(n) time & O(n) space

        totalSize=len(nums)
        freq=Counter(nums)
        mostFreq=max(freq.items(),key=lambda x:x[1])[0]
        # mostFreq = max(freq, key=freq.get)
        indices=[i for i,num in enumerate(nums) if num==mostFreq]
        

        for i in range(len(indices)):
            leftFreqSize=i+1
            rightFreqSize=len(indices)-leftFreqSize

            #formulated from first time :)
            #dominance condition: dominant_count * 2 > subarray_size
            if (2*leftFreqSize>indices[i]+1) and (2*rightFreqSize>totalSize-indices[i]-1):
                return indices[i]

        return -1
