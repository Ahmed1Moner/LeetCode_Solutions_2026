#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Language: python3
# Date: 2026-03-07


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #sol 5: O(n) time & O(n) space

        if not nums:
            return 0

        def dfs(node):
            seen.add(node)
            length=1
            for neighbor in adjs[node]:
                if neighbor not in seen:
                    length+=dfs(neighbor)

            return length

        
        nums,seen=set(nums),set()
        adjs=defaultdict(list)
        longest=0

        for num in nums:
            if (num+1) in nums:
                adjs[num].append(num+1)
                adjs[num+1].append(num)

        
        for num in nums:
            if num not in seen:
                longest=max(longest,dfs(num))

        return longest





        #sol 4: O(n) time & O(n) space
        
        nums=set(nums)
        longest=0

        for num in nums:
            if (num-1) not in nums:
                length=1

                while (num+1) in nums:
                    length+=1
                    num+=1

                longest=max(longest,length)

        return longest




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
