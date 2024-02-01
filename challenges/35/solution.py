def searchInsert(nums, target):

    # array of 1 element
    if len(nums) == 1:
        if target > nums[0]:
            return 1
        else:
            return 0
        
    index = 0
    start = 0
    end = len(nums) - 1

    # binary search
    done = False
    while not done:
        middle = int((end + start) / 2)

        # target
        if target == nums[middle]:
            # done!
            return middle

        # only two elements remain
        elif (end - start) == 1:
            if target < nums[start]:
                return start
            elif target > nums[end]:
                return end + 1
            else:
                return end

        elif target < nums[middle]:
            # go left!
            end = middle

        else:
            # go right!
            start = middle

    return index
