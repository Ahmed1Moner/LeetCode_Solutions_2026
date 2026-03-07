#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Language: python3
# Date: 2026-03-07


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #sol 3: O(n) time & O(n) space

        nums,seen=set(nums),set()
        ans=0

        for num in nums:
            if num not in seen:
                seen.add(num)
                ctr=1

                left=num-1
                while left not in seen and left in nums:
                    ctr+=1
                    seen.add(left)
                    left-=1

                right=num+1
                while right not in seen and right in nums:
                    ctr+=1
                    seen.add(right)
                    right+=1
                
                ans=max(ans,ctr) #longest sequence
                
        return ans



        #sol 2: O(nlogn) time & O(1) space
        
        if not nums:
            return 0

        nums.sort()
        ctr,maxVal=1,1

        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            elif nums[i+1]-nums[i]==1:
                ctr+=1
            else:
                maxVal=max(maxVal,ctr)
                ctr=1

        return max(maxVal,ctr)



        #sol 1: O(nlogn) time & O(n) space

        if not nums:
            return 0

        uni=list(set(nums))
        uni.sort()

        ctr,maxVal=1,1
        for i in range(len(uni)-1):
            if uni[i+1]-uni[i]==1:
                ctr+=1
            else:
                maxVal=max(maxVal,ctr)
                ctr=1

        maxVal=max(maxVal,ctr) #must update if there's no a gap, reached the end-> don't return ctr but update hte maxVal
        return maxVal
