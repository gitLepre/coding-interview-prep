from typing import List

def maxArea(height: List[int]) -> int:
    rx_bound = height[-1]
    lx_bound = height[0]

    rx_index = len(height)-1
    lx_index = 0

    area = min(rx_bound, lx_bound) * (rx_index - lx_index)

    while lx_index != rx_index:

        # start where the bound is smaller, find a new bound

        # rx < lx, move rx index
        if rx_bound < lx_bound:
            rx_index -= 1

            # if new line is > bound, line became a new bound
            if rx_bound < height[rx_index]:
                rx_bound = height[rx_index]

        # lx < rx, move lx index
        else:
            lx_index += 1
            
            # if new line is > bound, line became a new bound
            if lx_bound < height[lx_index]:
                lx_bound = height[lx_index]

        # check if area is increased if
        new_area = min(rx_bound, lx_bound) * (rx_index - lx_index)
        if new_area > area:
            area = new_area
    
    return area
    