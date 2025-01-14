class Solution(object):
    def mySqrt(self, x):
        if x==0 or x==1:
            return x
        # if x==3:
        #     return 1
        n = x//2
        left,right = 0,n
        while left<=right:
            mid = left+(right-left)//2
            if mid*mid>x:
                right = mid-1
            elif mid*mid<x:
                left = mid+1
            else:
                return mid
        return left -1

x = Solution()
print(x.mySqrt(3))