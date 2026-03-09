#
# Problem: 2570. Merge Two 2D Arrays by Summing Values
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=problem-list-v2&envId=waksgnnd
# Language: python3
# Date: 2026-03-09


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        #sol 1: O(n) time & O(n) space

        i,j,size1,size2=0,0,len(nums1),len(nums2)
        res=[]

        while i<size1 and j<size2:
            id1,val1,id2,val2=nums1[i][0],nums1[i][1],nums2[j][0],nums2[j][1]

            if id1==id2:
                res.append([id1,val1+val2])
                i+=1
                j+=1

            elif id1<id2:
                res.append([id1,val1])
                i+=1
            
            else:
                res.append([id2,val2])
                j+=1

        if i<size1:
            res.extend(nums1[i:])
        elif j<size2:
            res.extend(nums2[j:])

        return res
