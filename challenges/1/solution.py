def twoSum(self, nums, target):
    
    if(len(nums)!=2):        
        pos = 0
        nums_dict = {}
        for num in nums:
            if target-num in nums_dict:
                # bingo!
                return [pos, nums_dict[target-num]]
            nums_dict[num]=pos    
            pos+=1

    # best case
    return [0,1]