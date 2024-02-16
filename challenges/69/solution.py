def mySqrt(self, x: int) -> int:
    # y = sqrt(x)
    # y*y = x

    if(x == 1):
        return x

    start = 0
    end = x
    y = round(x/2)

    stop = False
    while(not stop):
        
        # without remainder
        if(y*y) == x:
            return y

        if (y*y) > x:
            end = y
        else:  
            start = y      

            # with remainder
            # y*y <= x --> already checked
            # (y+1)*(y+1) > x
            if ( (y+1)*(y+1) > x ):
                return y

        # update y
        y = round((start + end)/2)