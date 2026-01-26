#
# Problem: 2496. Maximum Value of a String in an Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/?envType=problem-list-v2&envId=w95808hv
# Language: python3
# Date: 2026-01-26


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        #O(n*k) time & O(1) space -> k:avg length of the string

        return max(int(s) if s.isdigit() else len(s) for s in strs)
