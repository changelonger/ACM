"""
给定一个二维数组 array，请返回「螺旋遍历」该数组的结果。

螺旋遍历：从左上角开始，按照 向右、向下、向左、向上 的顺序 依次 提取元素，然后再进入内部一层重复相同的步骤，直到提取完所有元素。

 

示例 1：

输入：array = [[1,2,3],[8,9,4],[7,6,5]]
输出：[1,2,3,4,5,6,7,8,9]
示例 2：

输入：array  = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
输出：[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
不一定是正方形
"""
class Solution(object):
    def spiralArray(self, array):
        arr = []  # 存放结果的数组
        if not array:
            return arr
        a = len(array)  # 行数
        b = len(array[0])  # 列数
        startx, starty = 0, 0  # 左上角坐标
        end = 0  # 控制边界的变量，初始值是 0
        count = a * b  # 总元素数
        while count > 0:
            # 从左到右遍历上边
            for j in range(starty, b - end):
                arr.append(array[startx][j])
                count -= 1
            # 从上到下遍历右边
            for i in range(startx + 1, a - end):
                arr.append(array[i][b - end - 1])
                count -= 1
            # 从右到左遍历下边
            if startx < a - end - 1:  # 确保下边存在
                for j in range(b - end - 2, starty - 1, -1):
                    arr.append(array[a - end - 1][j])
                    count -= 1
            # 从下到上遍历左边
            if starty < b - end - 1:  # 确保左边存在
                for i in range(a - end - 2, startx, -1):
                    arr.append(array[i][starty])
                    count -= 1
            
            # 更新边界
            startx += 1
            starty += 1
            end += 1
        
        return arr
