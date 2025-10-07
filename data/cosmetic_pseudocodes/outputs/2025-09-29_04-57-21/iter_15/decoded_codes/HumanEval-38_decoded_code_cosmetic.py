from typing import List


def encode_cyclic(input_string: str) -> str:
    groups_collection: List[str] = []
    limit: int = (len(input_string) + 2) // 3

    for counter in range(limit):
        start_idx: int = counter * 3
        end_idx: int = min(start_idx + 3, len(input_string))
        groups_collection.append(input_string[start_idx:end_idx])

    transformed_groups: List[str] = []
    for item in groups_collection:
        if len(item) == 3:
            cyclic_shift: str = item[1:] + item[0]
            transformed_groups.append(cyclic_shift)
        else:
            transformed_groups.append(item)

    concatenated_output: str = ''.join(transformed_groups)
    return concatenated_output


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))