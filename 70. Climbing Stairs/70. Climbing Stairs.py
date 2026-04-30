#
# Problem: 70. Climbing Stairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/climbing-stairs/
# Language: python3
# Date: 2026-04-30


class Solution:
    def climbStairs(self, n: int) -> int:

        #Sol 4: Space O(n) time & O(n) space

        if n==0 or n==1:
            return 1

        prev,curr=1,2
        for i in range(3,n+1):
            prev,curr=curr,prev+curr
        
        return curr


        #Sol 3: Memoization O(n) time & O(n) space

        dp={}
        return self.helper(n,dp)

    def helper(self,n,dp):
        if n==0 or n==1:
            return 1
        
        if n not in dp:
            dp[n]=self.helper(n-1,dp)+self.helper(n-2,dp)

        return dp[n]



        #Sol 2: Tabulation O(n) time & O(n) space

        if n==1:
            return 1

        dp=[0]*(n+1)
        dp[1],dp[2]=1,2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]


        #Sol 1: Recursion TLE O(2^n) time & O(n) space

        #base case
        if n==1:
            return 1

        #recursion case
        return self.climbStairs(n-1) + self.climbStairs(n-2)        

