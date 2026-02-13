#
# Problem: 287. Find the Duplicate Number
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-duplicate-number/description/
# Language: python3
# Date: 2026-02-13


#try bit manipulation

#wow: check those solutions: https://leetcode.com/problems/find-the-duplicate-number/solutions/4918970/one-line-solution-by-mikposp-o88y

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #sol 5: O(n) time & O(1) space
        
        for i in range(len(nums)):
            idx=abs(nums[i])
            
            if nums[idx]<0:
                return idx
            nums[idx]*=-1

        return -1


        #sol 4: O(nlogn) time & O(1) space

        nums.sort()
        return next((nums[i] for i in range(len(nums)-1) if nums[i]==nums[i+1]),-1)


        #sol 3: O(n) time & O(n) space

        mapp=Counter(nums)
        for k,v in mapp.items():
            if v>1:
                return k


        #sol 2: O(n) time & O(n) space

        sett=set()
        for num in nums:
            if num in sett:
                return num
            sett.add(num)


        #sol 1: brute force TLE: O(n^2) time & O(1) space

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return nums[i]

        return -1
