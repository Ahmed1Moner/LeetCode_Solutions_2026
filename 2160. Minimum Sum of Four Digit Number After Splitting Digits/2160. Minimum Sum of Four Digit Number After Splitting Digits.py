#
# Problem: 2160. Minimum Sum of Four Digit Number After Splitting Digits
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# Language: python3
# Date: 2026-01-26


class Solution:
    def minimumSum(self, num: int) -> int:
        
        #Sol 2: O(nlogn) time & O(n) space

        digits=sorted(map(int,str(num)))
        return digits[-1]+10*digits[0] + digits[-2]+10*digits[1]



        #Sol 1: brute force O(n) time & O(1) space

        num=list(str(num))
        maxVal1=max(num)
        num.remove(maxVal1)
        # del num[num.index(maxVal1)]
        maxVal2=max(num)
        num.remove(maxVal2)
        
        return int(maxVal1)+10*int(num[0])+int(maxVal2)+10*int(num[1])
