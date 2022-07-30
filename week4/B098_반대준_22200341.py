class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            nums[int(i)-1]=str(nums[int(i)-1]) 
        return [i+1 for i in range(len(nums))  if type(nums[i])==int]