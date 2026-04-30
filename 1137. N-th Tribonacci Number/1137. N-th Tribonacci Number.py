#
# Problem: 1137. N-th Tribonacci Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/n-th-tribonacci-number/submissions/1992144887/
# Language: python3
# Date: 2026-04-30


class Solution:
    def tribonacci(self, n: int) -> int:

        #Sol 4: Space O(n) time & O(n) space

        if n==0 or n==1:
            return n

        last,prev,curr=0,1,1

        for i in range(3,n+1):
            last,prev,curr=prev,curr,last+prev+curr

        return curr


        #Sol 3: Memoization O(n) time & O(n) space

        dp={}
        return self.helper(n,dp)

    def helper(self,n,dp):
        
        if n==0:
            return 0
        if n==1 or n==2:
            return 1

        if n not in dp:
            dp[n]=self.helper(n-1,dp)+self.helper(n-2,dp)+self.helper(n-3,dp)

        return dp[n]


        #Sol 2: Tabulation O(n) time & O(n) space

        if n==0:
            return 0
        if n==1 or n==2:
            return 1

        dp=[0]*(n+1)
        dp[1],dp[2]=1,1

        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

        return dp[n]


        #Sol 1: TLE Recursion O(2^n) & O(n) space

        if n==0:
            return 0
        if n==1 or n==2:
            return 1

        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

