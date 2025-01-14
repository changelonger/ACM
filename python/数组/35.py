"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
nums为 无重复元素 的 升序 排列数组
示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""
def fun(nums,target):
    left,right = 0,len(nums)-1
    while left<=right:
        mid = left+(right-left)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]>target:
            right = mid-1
        else:
            return mid
    return left  #或者 return right+1
    # 因为left到最后在right的右边，而target此时是在[right,left]中间所以要插入后面，return left，或者 return right+1