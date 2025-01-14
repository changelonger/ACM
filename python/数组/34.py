"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
"""

class Solution(object):
    def searchRange(self, nums, target):
        def searchleft(nums,traget):
            left,right = 0,len(nums)-1
            while left<=right:
                mid = (right-left)//2+left
                if nums[mid]==target:
                    if mid==0 or nums[mid-1] <target:
                        return mid
                    else :
                        right = mid-1
                elif nums[mid]>=target:
                    right = mid-1
                else :
                    left = left+1
            return -1
        def searchright(nums,target):
            left,right = 0,len(nums)-1
            while left<=right:
                mid = left+(right-left)//2
                if nums[mid]>target:
                    right = mid-1
                elif nums[mid]<target:
                    left = mid+1
                else:
                    if mid == len(nums)-1 or  nums[mid+1]>target:
                        return mid
                    else:
                        left = mid+1
            return -1
        left = searchleft(nums,target)
        right = searchright(nums,target)
        return [left,right]


                    
    