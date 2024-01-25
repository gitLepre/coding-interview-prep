def plusOne(digits):
    carry = 1
    i = len(digits)-1
    while(i >= 0):
        digits[i] = (digits[i] + carry) % 10

        carry = 1 if digits[i] == 0 else 0

        if(not carry):
            # no carry, we're done
            return digits
        i -= 1
    
    # insert leading 1 if carry is still 1
    digits.insert(0, 1)
    return digits
