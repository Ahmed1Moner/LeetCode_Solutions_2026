#
# Problem: 441. Arranging Coins
# Difficulty: Easy
# Link: https://leetcode.com/problems/arranging-coins/description/
# Language: python3
# Date: 2026-02-13


class Solution:

    def arrangeCoins(self, n: int) -> int:

        #sol 2: O(logn) time * O(1) space

        left,right=0,n
        while left<=right:
            mid=left+(right-left)//2
            coins=mid*(mid+1)//2

            if coins <= n:
                left=mid+1
                ans=mid

            else:
                right=mid-1

        return ans


        #brute force: TLE O(n) time & O(1) space

        ctr=0
        for i in range(1,n+1):
            if n-i>=0:
                n-=i
                ctr+=1

        return ctr
