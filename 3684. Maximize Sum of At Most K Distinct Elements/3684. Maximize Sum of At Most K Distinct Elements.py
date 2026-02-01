#
# Problem: 3684. Maximize Sum of At Most K Distinct Elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/?envType=problem-list-v2&envId=waksgnnd
# Language: python3
# Date: 2026-02-01


#try heap

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:

      #sol 1: O(nlogn) time & O(n) space

      return sorted(set(nums), reverse=True)[:k]
