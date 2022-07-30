class Solution:
    def searchInsert(self, nums, target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)