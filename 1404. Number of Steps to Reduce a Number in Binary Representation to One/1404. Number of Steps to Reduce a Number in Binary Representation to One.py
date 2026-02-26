#
# Problem: 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2026-02-26
# Language: python3
# Date: 2026-02-26


class Solution:
    def numSteps(self, s: str) -> int:
        

        #sol 2: O(n) time and O(n) space

        steps=0
        s=list(s)

        while not (len(s)==1 and s[-1]=='1'):
            if s[-1]=='0':
                s.pop()

            else:
                j=len(s)-1
                while j>=0 and s[j]=='1':
                    s[j]='0'
                    j-=1
                
                if j<0:
                    s=['1']+s
                    # s.insert(0,'1')
                else:
                    s[j]='1'
            
            steps+=1
        return steps




        #sol 1: O(n^2) time and O(n) space wow!

        steps=0
        num=int(s,2) #py stores big integers as arrays of machine words

        while num!=1: #O(n) time
            num = num+1 if num%2==1 else num//2 #O(n) time for big integers
            steps+=1

        return steps
