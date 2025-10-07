def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        reversed_string = ""
        index = len(s) - 1
        while index >= 0:
            reversed_string += s[index]
            index -= 1
        return reversed_string
    else:
        right_part = ""
        start_right = len(s) - shift
        index_right = start_right
        while index_right < len(s):
            right_part += s[index_right]
            index_right += 1
        left_part = ""
        index_left = 0
        while index_left < start_right:
            left_part += s[index_left]
            index_left += 1
        result = right_part + left_part
        return result