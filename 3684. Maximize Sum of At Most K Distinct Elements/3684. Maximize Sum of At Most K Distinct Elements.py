#
# Problem: 3684. Maximize Sum of At Most K Distinct Elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/description/?envType=problem-list-v2&envId=waksgnnd
# Language: python3
# Date: 2026-02-01


#try heap

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:

        #sol 2: O(nlogn) time & O(K)~O(1) space

        nums.sort(reverse=True)

        res=[nums[0]]
        k-=1
        i=1

        while k>0 and i<len(nums):
            if nums[i]!=nums[i-1]:
                res.append(nums[i])
                k-=1
            i+=1

        return res



        #sol 1: O(nlogn) time & O(n) space

        return sorted(set(nums), reverse=True)[:k]
