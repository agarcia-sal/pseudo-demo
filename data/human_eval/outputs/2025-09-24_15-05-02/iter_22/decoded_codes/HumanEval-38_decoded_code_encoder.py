from typing import List


def encode_cyclic(input_string: str) -> str:
    group_list: List[str] = []
    number_of_groups: int = (len(input_string) + 2) // 3

    for group_index in range(number_of_groups):
        start_index: int = 3 * group_index
        end_index: int = min(start_index + 3, len(input_string))
        current_group: str = input_string[start_index:end_index]
        group_list.append(current_group)

    for index in range(len(group_list)):
        if len(group_list[index]) == 3:
            group_list[index] = group_list[index][1:] + group_list[index][0]

    encoded_string: str = "".join(group_list)
    return encoded_string


def decode_cyclic(encoded_string: str) -> str:
    return encode_cyclic(encode_cyclic(encoded_string))