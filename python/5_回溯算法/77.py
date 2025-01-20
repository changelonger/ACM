"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。你可以按 任何顺序 返回答案。
示例 1：
输入：n = 4, k = 2
输出：
[
[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],
]
示例 2：
输入：n = 1, k = 1
输出：[[1]]
"""
class Solution(object):
    def combine(self, n, k):
        res = []
        self.dfs(n, k, 1, [], res)
        return res

    def dfs(self, n, k, start, path, res):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n+1):
            path.append(i)
            self.dfs(n, k, i + 1, path, res)
            path.pop()


