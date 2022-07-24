def findDisappearedNumbers(nums) :
    for i in range(len(nums)):
        index = abs(nums[i])-1
        nums[index] = -1*nums[index] if nums[index]>0 else nums[index]
    return [i+1 for i in range(len(nums)) if nums[i]>0]