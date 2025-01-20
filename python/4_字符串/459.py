"""
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
示例 1:

输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。
示例 2:

输入: s = "aba"
输出: false
示例 3:

输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
"""
# 方法一
class Solution(object):
    def repeatedSubstringPattern(self, s):
        ss = s[1:] + s[:-1]
        return ss.find(s) != -1



# 方法二需要用kmp
class Solution(object):
    def get_next(self, s, next):
        j = 0
        next[0] = 0
        for i in range(len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return next

    def repeatedSubstringPattern(self, s):
        next = [0] * len(s)
        self.get_next(s, next)
        if next[-1] != -1 and len(s) % (len(s) - (next[-1] + 1)) == 0:
            return True
        return False





