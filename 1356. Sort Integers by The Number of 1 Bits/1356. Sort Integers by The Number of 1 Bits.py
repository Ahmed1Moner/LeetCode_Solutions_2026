#
# Problem: 1356. Sort Integers by The Number of 1 Bits
# Difficulty: Easy
# Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=daily-question&envId=2026-02-25
# Language: python3
# Date: 2026-02-25


#try bucket sort & dp

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        #sol 2: O(nlogn) time & O(1) space

        arr.sort(key=lambda x: (x.bit_count() ,x))
        return arr


        #sol 1: O(nlogn) time & O(n) space

        arr.sort()
        ans=[]
        for i in range(len(arr)):
            ans.append((bin(arr[i]).count('1') ,arr[i]))

        ans2=sorted(ans, key=lambda x:x[0])
        
        return [j for _,j in ans2]
