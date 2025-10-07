def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        result = ""
        index = len(s) - 1
        while index >= 0:
            result += s[index]
            index -= 1
        return result
    else:
        length = len(s)
        first_part = ""
        second_part = ""
        index = length - shift
        while index < length:
            second_part += s[index]
            index += 1
        index = 0
        while index < length - shift:
            first_part += s[index]
            index += 1
        return second_part + first_part