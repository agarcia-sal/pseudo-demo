def circular_shift(x, shift):
    s = str(x)
    length_s = len(s)
    if shift > length_s:
        result = ''
        index = length_s - 1
        while index >= 0:
            result += s[index]
            index -= 1
        return result
    else:
        part_one = ''
        start_index_part_one = length_s - shift
        index_part_one = start_index_part_one
        while index_part_one < length_s:
            part_one += s[index_part_one]
            index_part_one += 1
        part_two = ''
        index_part_two = 0
        while index_part_two < start_index_part_one:
            part_two += s[index_part_two]
            index_part_two += 1
        result = part_one + part_two
        return result