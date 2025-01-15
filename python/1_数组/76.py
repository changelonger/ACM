"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 
示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""
from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        ht = defaultdict(int)  # 目标字符串 t 中字符的频次
        hs = defaultdict(int)  # 当前窗口中字符的频次
        
        # 构建 t 的字符频次表
        for char in t:
            ht[char] += 1
        
        left = 0
        distance = 0  # 当前窗口满足条件的字符种类数
        min_len = float('inf')  # 初始化最小窗口长度为正无穷
        min_left = 0  # 记录最小窗口的起始位置
        
        for right in range(len(s)):
            hs[s[right]] += 1  # 增加当前字符的频次
            
            # 如果当前字符的频次不超过 t 中该字符的频次，增加distance
            if hs[s[right]] <= ht[s[right]]:
                distance += 1
            
            # 当当前窗口满足条件时，尝试缩小窗口
            while distance == len(t):
                # 更新最小窗口长度
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # 缩小窗口，移动左指针
                hs[s[left]] -= 1
                if hs[s[left]] < ht[s[left]]:
                    distance -= 1
                left += 1
        
        # 如果最小窗口没有更新，说明没有符合条件的子串，返回空字符串
        if min_len == float('inf'):
            return ""
        
        return s[min_left:min_left + min_len]
