class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        fast = 1
        slow = 1
        n = len(nums)
        while fast<n:
            if nums[fast]!=nums[fast-1]:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow