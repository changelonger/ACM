"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""
class Solution(object):
    def subsets(self, nums):
        res, path, n = [], [], len(nums)
        """
        
        """
        def dfs(i):
            res.append(path[:])
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return res
    """
    遍历过程空集 ， 0 01 012 0123
                       013
                    02 023
                    03
                  1 12 123
                    13
                  2 23
                  3
    """




