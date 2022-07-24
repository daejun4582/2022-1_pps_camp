def singleNumber(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]= 1
        else:
            dic[i]+=1
    for j in nums:
        if dic[j]==1:
            return j
    