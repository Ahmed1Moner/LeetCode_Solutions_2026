#
# Problem: 1619. Mean of Array After Removing Some Elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
# Language: python3
# Date: 2026-01-25


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        #Sol 1: O(nlogn) time & O(n) space

        ratio=len(arr)//20
        arr.sort()

        piece=arr[ratio:-ratio]
        return sum(piece)/len(piece) #normal iteration instead of sum for O(1) space

        # return sum(arr[ratio:-ratio]) / (len(arr)-ratio*2)

