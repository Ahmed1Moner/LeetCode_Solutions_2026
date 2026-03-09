#
# Problem: 2656. Maximum Sum With Exactly K Elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/?envType=problem-list-v2&envId=waksgnnd
# Language: python3
# Date: 2026-03-09


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        #sol 3: O(n) time & O(1) space

        m=max(nums)
        return m*k + (k*(k-1))//2

        
        #sol 2: O(n+k)~O(n) time & O(1) space

        maxVal=max(nums)
        return sum((maxVal:=maxVal+1)-1 for _ in range(k)) #-1: add the previous maxVal value

        #sol 1: O(n+k)~O(n) time & O(1) space

        summ,maxVal=0,max(nums)
        while k!=0:
            summ+=maxVal
            maxVal+=1
            k-=1
        return summ
