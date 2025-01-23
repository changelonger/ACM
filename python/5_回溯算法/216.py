"""
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
只使用数字1到9
每个数字 最多使用一次
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了
"""


class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        path = []

        def dfs(i, sum):
            if len(path) == k:
                if sum == n:
                    res.append(path[:])
                return
            for j in range(i, 10):
                path.append(j)
                dfs(j + 1, sum + j)
                path.pop()

        dfs(1, 0)
        return res

