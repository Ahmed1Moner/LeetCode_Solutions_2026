#
# Problem: 1283. Find the Smallest Divisor Given a Threshold
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/submissions/1917641568/
# Language: python3
# Date: 2026-02-13


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        #sol 1: O(logn) time & O(1) space

        left,right=1,max(nums)
        while left<=right:
            
            mid=left+(right-left)//2
            summ=sum(math.ceil(num/mid) for num in nums)

            if summ > threshold:
                left=mid+1

            else:
                right=mid-1
                ans=mid

        return ans
