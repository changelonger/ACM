"""
给定两个字符串 s 和 p，找到 s 中所有 p 的
异位词
 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
"""
from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []

        n = len(p)
        hp = Counter(p)
        left = 0
        right = n
        res = []

        # 初始化滑动窗口的频率计数
        hs = Counter(s[left:right])

        # 判断第一个窗口是否符合
        if hs == hp:
            res.append(left)

        # 滑动窗口
        while right < len(s):
            # 移除左边的字符
            hs[s[left]] -= 1
            if hs[s[left]] == 0:
                del hs[s[left]]  # 删除频率为 0 的字符

            # 移动右边界
            right += 1

            # 添加右边新字符
            hs[s[right - 1]] += 1

            # 判断当前窗口是否与 p 的字符频率相同
            if hs == hp:
                res.append(left + 1)

            # 移动左边界
            left += 1

        return res
