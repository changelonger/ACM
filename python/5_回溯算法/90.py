"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的
子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        res, path, n = [], [], len(nums)

        def dfs(i):
            res.append(path[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return res
