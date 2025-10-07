def circular_shift(x, shift):
    s = str(x)
    length = len(s)
    if shift > length:
        result = ''
        for i in range(length - 1, -1, -1):
            result += s[i]
        return result
    else:
        first_part = ''
        second_part = ''
        start_index = length - shift
        for i in range(start_index, length):
            second_part += s[i]
        for i in range(start_index):
            first_part += s[i]
        return second_part + first_part