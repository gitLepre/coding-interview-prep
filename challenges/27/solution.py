def removeElement(self, nums, val: int) -> int:
    # in place --> no new array

    # 2 pointers
    start = 0
    end = len(nums)-1

    k = len(nums)

    while(end>=start):
        if nums[start] == val:
            # move to end
            temp = nums[end]
            nums[end] = -1
            nums[start] = temp
            end-=1
            k-=1

        else:
            start+=1
    return k

        



 
        