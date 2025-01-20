class Solution(object):
    def letterCombinations(self, digits):
        map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        n = len(digits)
        if n == 0:
            return []
        tem = []
        res = []
        path = [''] * n
        for char in digits:
            tem.append(map[int(char)])
        def dfs(i):
            if i == n:
                res.append(''.join(path))
                return
            for c in tem[i]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return res


