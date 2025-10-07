def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        result = []
        for index in range(len(s) - 1, -1, -1):
            current_char = s[index]
            result.append(current_char)
        reversed_string = ''.join(result)
        return reversed_string
    else:
        length = len(s)
        first_part_start = length - shift
        first_part = []
        for index in range(first_part_start, length):
            current_char = s[index]
            first_part.append(current_char)
        second_part = []
        for index in range(0, first_part_start):
            current_char = s[index]
            second_part.append(current_char)
        shifted_string = ''.join(first_part) + ''.join(second_part)
        return shifted_string