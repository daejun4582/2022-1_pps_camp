def summaryRanges( nums) :
    count=0
    start = 0
    l =[]
    result = []
    for i in range(len(nums)):
        if i <len(nums)-1:
            if count ==0:
                if nums[i]+1==nums[i+1]:
                    count+=1
                    start = i
                else:
                    l.append(i)
            else:
                if nums[i]+1== nums[i+1]:
                    count+=1
                else:
                    print(start,count)
                    l.append([start,count])
                    count = 0
        else:
            if count ==0:
                l.append(i)
            else:
                l.append([start,count])
                
    for i in range(len(l)):
       if isinstance(l[i],list):
           result.append(str(nums[l[i][0]])+"->"+str(nums[l[i][0]+l[i][-1]]))
       else:
           result.append(str(nums[l[i]]))
    
    return result                
   
                
            
           
        
nums = [0,1,2,4,5,7]
print(summaryRanges(nums))