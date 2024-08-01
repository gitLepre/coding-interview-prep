def convert(s: str, numRows: int) -> str:
    # scorrere la string num_rows volte
    # ogni volta ti sposti avanti di (num_rows-1)*2
    idx = 0
    row = 0
    total_step = (numRows-1)*2
    is_first_step = True

    # edge cases
    output = s[0]
    if len(s) == 1:
        return output
    if len(s) < numRows:
        return s
    if numRows == 1:
        return s


    while(True):
        
        first_step = (numRows-1-row)*2
        second_step = total_step - first_step
        do_step = False

        # first step
        if is_first_step:
            is_first_step = False
            if first_step != 0:
                do_step = True
                idx += first_step
    

        # second step
        else:
            is_first_step = True
            if second_step != 0:
                do_step = True
                idx += second_step


        # restart with new line
        if idx >= len(s):

            row += 1

            if row >= numRows:
                break
            
            # reset index 
            is_first_step = True
            idx = row
            output += s[idx] # add first 
            continue
        
    
        # add char to the string
        if do_step:
            output += s[idx]

    return output

