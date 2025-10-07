def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    number_of_groups = (length_s + 2) // 3
    for i in range(number_of_groups):
        start_index = 3 * i
        end_index = 3 * i + 3 if 3 * i + 3 < length_s else length_s
        substring = s[start_index:end_index]
        groups.append(substring)
    for index in range(len(groups)):
        group = groups[index]
        if len(group) == 3:
            first_char = group[0]
            remaining_chars = group[1:3]
            new_group = remaining_chars + first_char
            groups[index] = new_group
        else:
            groups[index] = group
    result = ''
    for index in range(len(groups)):
        result += groups[index]
    return result

def decode_cyclic(s: str) -> str:
    first_encoding = encode_cyclic(s)
    second_encoding = encode_cyclic(first_encoding)
    return second_encoding