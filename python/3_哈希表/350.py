"""
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
可以不考虑输出结果的顺序。
示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
"""
# 方法一
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        nums = list(set(nums1) & set(nums2))
        h1 = Counter(nums1)
        h2 = Counter(nums2)
        res = []
        for i in nums:
            cnt = min(h1[i], h2[i])
            res.extend([i] * cnt) # extend的作用是添加重复的n个元素进去
        return res

# 方法2
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list((Counter(nums1) & Counter(nums2)).elements())

#  (Counter(nums1) & Counter(nums2)取两个 Counter 对象中相同元素的最小计数
#  elements() 是 Counter 类的方法，返回一个迭代器，该迭代器可以生成所有计数大于 0 的元素，
#  每个元素会按它在 Counter 中的计数次数重复
