def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        reversed_string = ''
        index = len(s) - 1
        while index >= 0:
            reversed_string += s[index]
            index -= 1
        return reversed_string
    else:
        length = len(s)
        right_part = ''
        i = length - shift
        while i < length:
            right_part += s[i]
            i += 1
        left_part = ''
        j = 0
        while j < length - shift:
            left_part += s[j]
            j += 1
        return right_part + left_part