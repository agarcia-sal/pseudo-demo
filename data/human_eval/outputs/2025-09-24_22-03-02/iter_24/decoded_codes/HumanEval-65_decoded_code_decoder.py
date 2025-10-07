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
        length = len(s)
        first_part = ""
        second_part = ""
        index = length - shift
        while index < length:
            first_part += s[index]
            index += 1
        index = 0
        while index < length - shift:
            second_part += s[index]
            index += 1
        return first_part + second_part