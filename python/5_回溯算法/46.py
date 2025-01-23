"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""
class Solution(object):
    def permute(self, nums):
        res, path, n = [], [], len(nums)
        v = [0]*n
        def dfs(i):
            if len(path) == n:
                res.append(path[:])
                return
            for j in range(0, len(nums)):
                if v[j]==1:
                    continue
                path.append(nums[j])
                v[j]=1
                dfs(j + 1)
                path.pop()
                v[j]= 0

        dfs(0)
        return res
