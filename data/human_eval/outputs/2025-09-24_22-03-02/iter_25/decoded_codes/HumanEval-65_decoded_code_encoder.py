def circular_shift(x: int, shift: int) -> str:
    s = str(x)
    if shift > len(s):
        reversed_s = ''
        index = len(s) - 1
        while index >= 0:
            reversed_s += s[index]
            index -= 1
        return reversed_s
    else:
        length_s = len(s)
        first_part = ''
        second_part = ''
        index = length_s - shift
        while index < length_s:
            first_part += s[index]
            index += 1
        index = 0
        while index < length_s - shift:
            second_part += s[index]
            index += 1
        return first_part + second_part