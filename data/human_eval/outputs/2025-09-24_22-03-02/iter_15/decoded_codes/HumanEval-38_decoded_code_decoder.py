def encode_cyclic(s: str) -> str:
    groups = []
    length_of_s = len(s)
    number_of_groups = (length_of_s + 2) // 3
    for i in range(number_of_groups):
        start_index = 3 * i
        end_index = min(3 * i + 3, length_of_s)
        group = s[start_index:end_index]
        groups.append(group)
    cycled_groups = []
    for group in groups:
        if len(group) == 3:
            cycled_group = group[1:] + group[0]
            cycled_groups.append(cycled_group)
        else:
            cycled_groups.append(group)
    result = ''
    for element in cycled_groups:
        result += element
    return result

def decode_cyclic(s: str) -> str:
    first_encoding = encode_cyclic(s)
    second_encoding = encode_cyclic(first_encoding)
    return second_encoding