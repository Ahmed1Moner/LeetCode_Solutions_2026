#
# Problem: 436. Find Right Interval
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-right-interval/description/
# Language: python3
# Date: 2026-02-17


class Solution:

    def helper(self,lst,target):

        left,right,pos=0,len(lst)-1,-1

        while left<=right:
            mid=left+(right-left)//2

            if lst[mid][0]<target:
                left=mid+1
            
            else:
                right=mid-1
                pos=mid

        return pos


    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        ans=[-1]*len(intervals)

        startings=[(intervals[i][0],i) for i in range(len(intervals))]
        startings.sort()

        for i in range(len(intervals)):
            idx=self.helper(startings,intervals[i][1])

            if idx!=-1:
                ans[i]=startings[idx][1]

        return ans
