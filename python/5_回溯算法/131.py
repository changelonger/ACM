""""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：
输入：s = "a"
输出：[["a"]]
"""


class Solution(object):
    def partition(self, s):
        res = []
        path = []
        n = len(s)
        def dfs(i):
            if i == n:
                res.append(path[:])
                return
            for j in range(i, len(s)):
                t = s[i:j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return res




