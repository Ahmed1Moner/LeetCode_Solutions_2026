#
# Problem: 70. Climbing Stairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/climbing-stairs/submissions/1992137943/
# Language: python3
# Date: 2026-04-30


class Solution:
    def climbStairs(self, n: int) -> int:

        #sol1: O(n) time & O(n) space

        if n==1:
            return 1

        dp=[0]*(n+1)
        dp[1],dp[2]=1,2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
