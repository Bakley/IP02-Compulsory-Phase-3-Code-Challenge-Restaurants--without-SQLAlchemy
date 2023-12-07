def p_occurance(a, b, c):
    p_occurance = (a > 0) + (b > 0) + (c > 0)
    return p_occurance == 2

if __name__ == '__main__':
    pos_nums = p_occurance(-4, 6, 0)
    print(pos_nums)