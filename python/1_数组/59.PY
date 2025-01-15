"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 
"""

class Solution(object):
    def generateMatrix(self, n):
        nums = [[0]*n for _ in range(n)]
        count = 1
        end = 1
        startx,starty = 0,0
        for x in range(n//2):
            for j in range(starty,n-end):
                nums[starty][j]=count
                count+=1
            for i in range(startx,n-end):
                nums[i][n-end] = count
                count+=1
            for j in range(n-end,starty,-1):
                nums[n-end][j]=count
                count+=1
            for i in range(n-end,startx,-1):
                nums[i][startx] = count
                count+=1
            startx+=1
            starty+=1
            end+=1
        if n%2==1:
            nums[n//2][n//2] = n*n
        return nums
