class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [i, d[r]]
            d[j] = i
		
		# An Upvote will be encouraging