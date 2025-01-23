"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution(object):
    def permuteUnique(self, nums):
        res, path, n = [], [], len(nums)
        v = [0]*n
        nums = sorted(nums)
        def dfs(i):
            if len(path) == n:
                res.append(path[:])
                return
            for j in range(0, len(nums)):
                if v[j]==1:
                    continue
                if j>0 and nums[j]==nums[j-1] and v[j-1]==1:
                    continue
                path.append(nums[j])
                v[j]=1
                dfs(j + 1)
                path.pop()
                v[j]= 0
        dfs(0)
        return res