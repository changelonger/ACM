"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
示例 1：

输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""
class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return  s

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s[:] = s[::-1]  # 一行代码

