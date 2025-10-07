from typing import List

def encode_cyclic(s: str) -> str:
    groups: List[str] = []
    length_s = len(s)
    count_groups = (length_s + 2) // 3
    for i in range(count_groups):
        start_index = 3 * i
        if start_index + 3 < length_s + 1:
            end_index = start_index + 3
        else:
            end_index = length_s
        substring = ''
        for index in range(start_index, end_index):
            substring += s[index]
        groups.append(substring)
    cycled_groups: List[str] = []
    for group in groups:
        if len(group) == 3:
            cycled_group = ''
            for index in range(1, 3):
                cycled_group += group[index]
            cycled_group += group[0]
            cycled_groups.append(cycled_group)
        else:
            cycled_groups.append(group)
    result = ''
    for element in cycled_groups:
        result += element
    return result

def decode_cyclic(s: str) -> str:
    intermediate = encode_cyclic(s)
    result = encode_cyclic(intermediate)
    return result