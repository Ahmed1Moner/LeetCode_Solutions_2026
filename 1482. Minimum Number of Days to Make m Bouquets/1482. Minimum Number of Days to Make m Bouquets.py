#
# Problem: 1482. Minimum Number of Days to Make m Bouquets
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
# Language: python3
# Date: 2026-02-14


class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        #sol 3: O(n log maxDay) time & O(1) space

        def possible(day):

            flow,boq=0,0
            for bloom in bloomDay:
                if bloom<=day:
                    flow+=1
                    
                    if flow==k:
                        boq+=1
                        flow=0
                else:
                    flow=0

            return boq>=m

        if m*k>len(bloomDay):
            return -1

        left,right=min(bloomDay),max(bloomDay)

        while left<right:
            mid=left+(right-left)//2

            if possible(mid):
                right=mid
            else:
                left=mid+1

        return left



        #sol 2: brute force TLE: O(n^2) time & O(1) space

        #base case
        if m*k>len(bloomDay):
            return -1

        days=sorted(set(bloomDay))

        for day in days:
            flow,boq=0,0

            for bloom in bloomDay:
                if bloom<=day:
                    flow+=1

                    if flow==k:
                        boq+=1
                        flow=0

                else:
                    flow=0

            if boq>=m:
                return day

        return -1



        #sol 1: brute force TLE: O(max(bloomDay) * n) time & O(1) space

        #base case
        if m*k>len(bloomDay):
            return -1

        maxDay=max(bloomDay)

        for day in range(1,maxDay+1):
            boq,flow=0,0

            for bloom in bloomDay:
                if bloom <= day:
                    
                    flow+=1
                    if flow==k:
                        boq+=1
                        flow=0

                else:
                    flow=0

            if boq>=m:
                return day

        return -1
