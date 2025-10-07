from typing import List

def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    group_count = (len(input_string) + 2) // 3

    for i in range(group_count):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(input_string))
        group = input_string[start_index:end_index]
        groups.append(group)

    for index in range(len(groups)):
        if len(groups[index]) == 3:
            group = groups[index]
            cycled_group = group[1:] + group[0]
            groups[index] = cycled_group

    encoded_string = ''.join(groups)
    return encoded_string

def decode_cyclic(input_string: str) -> str:
    first_cycle = encode_cyclic(input_string)
    second_cycle = encode_cyclic(first_cycle)
    return second_cycle