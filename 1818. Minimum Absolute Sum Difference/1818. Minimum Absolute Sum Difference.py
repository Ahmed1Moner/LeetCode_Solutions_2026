#
# Problem: 1818. Minimum Absolute Sum Difference
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-absolute-sum-difference/?envType=problem-list-v2&envId=waksgnnd
# Language: python3
# Date: 2026-03-09


#try bisect_elft

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
       
        #sol 3: O(nlogn) time & O(n) space

        def bs(target):
            left,right=0,size-1
            while left<right:
                mid=left+(right-left)//2

                if newNums[mid]==target:
                    return abs(target-newNums[mid])

                if newNums[mid]<target:
                    left=mid+1
                else:
                    right=mid

            if left==0:
                return abs(target-newNums[left])
            else:
                return min(abs(target-newNums[left]), abs(target-newNums[left-1]))



        newNums=sorted(nums1)
        maxVal,size=float('inf'),len(nums1)
        summ=sum(abs(nums1[k]-nums2[k]) for k in range(size))

        for i in range(size):
            originalVal=abs(nums1[i]-nums2[i])
            closestVal=bs(nums2[i])

            maxVal=min(maxVal, summ - originalVal + closestVal)

        return min(maxVal,summ)%(10**9+7)

        
                
        #sol 2: TLE O(n^2) time & O(1) space

        minVal=float('inf')
        base=sum(abs(nums1[k]-nums2[k]) for k in range(len(nums1)))
        for i in range(len(nums1)):
            original=abs(nums1[i]-nums2[i])

            for j in range(len(nums2)):
                summ=base-original+abs(nums1[j]-nums2[i])
                minVal=min(minVal,summ)

        return minVal


        #sol 1: TLE O(n^3) time & O(1) space

        minVal=float('inf')
        for i in range(len(nums1)):
            original=nums1[i]
            for j in range(len(nums1)):

                nums1[i]=nums1[j]
                summ=sum(abs(nums1[k]-nums2[k]) for k in range(len(nums1)))
                minVal=min(minVal,summ)

            nums1[i]=original

        return minVal%(10**9+7)
