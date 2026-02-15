#
# Problem: 67. Add Binary
# Difficulty: Easy
# Link: https://leetcode.com/problems/add-binary/?envType=daily-question&envId=2026-02-15
# Language: python3
# Date: 2026-02-15


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        #sol 2: O(n) time & O(n) space

        return bin(int(a,2)+int(b,2))[2:]


        #sol 2: O(n^2) time & O(n) space

        def helper(ptr,carry):

            #base case
            if ptr<0:
                return '1' if carry==1 else ''
            
            #rec case
            summ=int(a[ptr])+int(b[ptr])+carry
            bit=str(summ%2)
            carry=1 if summ>1 else 0
            
            return helper(ptr-1, carry)+bit


        a,b=a.zfill(max(len(a),len(b))),b.zfill(max(len(a),len(b)))
        return helper(len(a)-1,0)



