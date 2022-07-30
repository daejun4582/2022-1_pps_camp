def search(self, nums, target: int) -> int:
    n = len(nums)
    
    if(target == nums[n // 2]):
        return n // 2
    elif(n == 1 and target != nums[0]):
        return -1
    elif(target < nums[n // 2]):   
        return self.search(nums[: n // 2] , target)
    else:
        temp = self.search(nums[n // 2 :] , target)
        if(temp == -1):
            return temp
        return n // 2 + temp