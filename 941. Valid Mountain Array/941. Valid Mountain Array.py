#
# Problem: 941. Valid Mountain Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-mountain-array/
# Language: python3
# Date: 2026-02-01


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        #sol 2: O(n) time & O(1) space
        
        if len(arr)<3: return False
        i,j=0,len(arr)-1

        while i<j:
            if arr[i]<arr[i+1]:
                i+=1
            
            if arr[j]<arr[j-1]:
                j-=1

            else:
                return False

        return i==j and i!=len(arr)-1 and j!=0



        #sol 1: O(n) time & O(1) space
        
        i,size=0,len(arr)
        if size<3: return False

        while i+1<size and arr[i]<arr[i+1]:
            i+=1
        
        #can't be first nor last element
        if i==0 or i==size-1: return False

        while i+1<size and arr[i]>arr[i+1]:
            i+=1

        return i==size-1
