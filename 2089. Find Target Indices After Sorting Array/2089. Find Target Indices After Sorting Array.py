#
# Problem: 2089. Find Target Indices After Sorting Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Language: python3
# Date: 2026-02-16


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        #sol 4: O(n) time & O(n) space

        less,equal=0,0
        for num in nums:
            if num<target:
                less+=1
            elif num==target:
                equal+=1

        return list(range(less,less+equal))



        #sol 3: O(nlogn) time & O(n) space

        nums.sort()        
        if target not in nums:
            return []
        ans=[]

        i=nums.index(target)
        while i<len(nums) and nums[i]==target:
            ans.append(i)
            i+=1

        return ans

        
        #sol 2: O(nlogn) time [nlogn sort + logn search + n iteration] & O(n) space
        
        nums.sort()
        left,right,found=0,len(nums)-1,-1

        while left<=right:
            mid=left+(right-left)//2

            if nums[mid]==target:
                found=mid
                break

            elif nums[mid]<target:
                left=mid+1

            else:
                right=mid-1

        if found==-1:
            return []

        ans=[]

        left=found
        while left>=0 and nums[left]==target:
            ans.append(left)
            left-=1

        right=found+1
        while right<len(nums) and nums[right]==target:
            ans.append(right)
            right+=1

        return sorted(ans)


        #sol 1: O(nlogn) time & O(n) space

        nums.sort()
        return [i for i,num in enumerate(nums) if num==target]
