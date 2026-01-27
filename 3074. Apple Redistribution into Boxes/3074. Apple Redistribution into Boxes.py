#
# Problem: 3074. Apple Redistribution into Boxes
# Difficulty: Easy
# Link: https://leetcode.com/problems/apple-redistribution-into-boxes/submissions/1898833097/?envType=problem-list-v2&envId=w95808hv
# Language: python3
# Date: 2026-01-27


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        #sol 2: O(nlogn) time & O(1) space

        totalApps=sum(apple)
        return next((i+1 for i,cap in enumerate(accumulate(sorted(capacity,reverse=True))) if cap>=totalApps), -1)

    

        #Sol 1: O(nlogn) time & O(1) space

        totalApps=sum(apple)
        capacity.sort(reverse=True)
        ctr=0
        
        for cap in capacity:
            totalApps-=cap
            ctr+=1

            if totalApps<=0:
                return ctr
        
        return -1
