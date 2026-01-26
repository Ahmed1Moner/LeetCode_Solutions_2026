#
# Problem: 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Language: python3
# Date: 2026-01-26


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #Sol 5: O(logn) time & O(logn) space

        def helper(left,right,flag):
            if left<=right:
                mid=left+(right-left)//2

                if nums[mid]==target:
                    if flag=='left':
                        newLeft=helper(left,mid-1,'left')
                        return mid if newLeft==-1 else newLeft
                    
                    else:
                        newRight=helper(mid+1,right,'right')
                        return mid if newRight==-1 else newRight


                elif nums[mid]<target:
                    return helper(mid+1,right,flag)
                
                else:
                    return helper(left,mid-1,flag)


            else:
                return -1

        
        left=helper(0,len(nums)-1,'left')
        right=helper(0,len(nums)-1,'right')
        
        return [left,right]


        
        # #Sol 4: O(logn) time & O(1) space

        # def findLeft(nums,target):
        #     left,right,ans=0,len(nums)-1,-1

        #     while left<=right:
        #         mid=left+(right-left)//2

        #         if nums[mid]==target:
        #             ans=mid
        #             right=mid-1
                
        #         elif nums[mid]<target:
        #             left=mid+1
                
        #         else:
        #             right=mid-1
            
        #     return ans


        # def findRight(nums,target):
        #     left,right,ans=0,len(nums)-1,-1

        #     while left<=right:
        #         mid=left+(right-left)//2
    
        #         if nums[mid]==target:
        #             ans=mid
        #             left=mid+1

        #         elif nums[mid]<target:
        #             left=mid+1

        #         else:
        #             right=mid-1

        #     return ans 

        # #find left and right edges separately
        # left=findLeft(nums,target)
        # right=findRight(nums,target)
        
        # return [left,right]



        
        # #Sol 3: brute force -> O(n) time & O(1) space -> binary search then traversal & new array of two positions only

        # left,right=0,len(nums)-1
        # while left<=right:
        #     mid=left+(right-left)//2

        #     #instead of return -> iterate with two pointers again to get the edges
        #     if nums[mid]==target:
        #         left,right=mid,mid
                
        #         while left-1>=0:
        #             if nums[left-1]==target:
        #                 left-=1
        #             else:
        #                 break
        #         while right+1<len(nums):
        #             if nums[right+1]==target:
        #                 right+=1
        #             else:
        #                 break
                
        #         return [left,right]


            
        #     elif nums[mid]<target:
        #         left=mid+1
            
        #     elif nums[mid]>target:
        #         right=mid-1
            
            
        # return [-1,-1]




        #Sol 2: brute force -> O(n) time & O(1) space
        return [next((i for i,num in enumerate(nums) if num==target),-1),
                next((i for i in range(len(nums)-1,-1,-1) if nums[i]==target),-1)]
                #or for i,num in reversed(list(enumerate(nums)))




        # #Sol 1: brute force -> O(n) time & O(1) space

        # ans=[-1,-1]

        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         ans[1]=i

        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i]==target:
        #         ans[0]=i
        
        # return ans
