"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

 

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
"""


class Solution(object):
    def moveZeroes(self, nums):
        fast,slow = 0,0
        n = len(nums)

        while fast<n:
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        i = slow
        while i<n:
            nums[i]=0
            i+=1

        