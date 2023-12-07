def clocky(hour, minute, period):
    # calculating 
    hour = (hour % 12 + (period.lower() == 'pm') * 12) % 24

    # the appearance of output
    result = "{:02d}{:02d}".format(hour, minute)
    return result
    
    
if __name__ == '__main__':
    
    four_digit = clocky(12, 43, 'pm')
    print(four_digit)
    
    four_digit_2 = clocky(12, 43, 'am')
    print(four_digit_2)
