"""
����һ�����շǵݼ�˳�����е��������� nums����һ��Ŀ��ֵ target�������ҳ�����Ŀ��ֵ�������еĿ�ʼλ�úͽ���λ�á�

��������в�����Ŀ��ֵ target������ [-1, -1]��

�������Ʋ�ʵ��ʱ�临�Ӷ�Ϊ O(log n) ���㷨��������⡣

 

ʾ�� 1��

���룺nums = [5,7,7,8,8,10], target = 8
�����[3,4]
ʾ�� 2��

���룺nums = [5,7,7,8,8,10], target = 6
�����[-1,-1]
ʾ�� 3��

���룺nums = [], target = 0
�����[-1,-1]
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


                    
    