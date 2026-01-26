#
# Problem: 1200. Minimum Absolute Difference
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-absolute-difference/?envType=daily-question&envId=2026-01-26
# Language: python3
# Date: 2026-01-26


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        #O(nlogn) time % O(n) space

        arr.sort()
        ans=[]

        minVal=float('inf')
        for i in range(1,len(arr)):
            minVal=min(minVal, abs(arr[i-1]-arr[i])) #take care not arr[1]-arr[0] after sorting: test case [1,3,5,6]


        for i in range(1,len(arr)):
            if abs(arr[i-1]-arr[i]) == minVal:
                ans.append([arr[i-1],arr[i]])
                i+=1
        
        return ans

