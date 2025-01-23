"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。
示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true
"""
from collections import defaultdict
from collections import Counter
# 解法1
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hm = defaultdict(int)
        hr = defaultdict(int)
        count = 0
        for char in ransomNote:
            hr[char]+=1
        for char in magazine:
            hm[char]+=1
            if hm[char]<=hr[char]:
                count+=1
        if count == len(ransomNote):
            return True
        else:
            return False

#解法2
class Solution:
    def canConstruct(self, ransomNote, magazine):
        return Counter(ransomNote) <= Counter(magazine)