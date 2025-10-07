from typing import List


def encode_cyclic(input_string: str) -> str:
    partitioned_strings: List[str] = []
    cursor: int = 0

    while cursor < len(input_string):
        end_pos = cursor + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        partitioned_strings.append(input_string[cursor:end_pos])
        cursor += 3

    transformed_groups: List[str] = []
    iterator: int = 0

    while iterator < len(partitioned_strings):
        segment = partitioned_strings[iterator]
        if len(segment) == 3:
            transformed_groups.append(segment[1:] + segment[0])
        else:
            transformed_groups.append(segment)
        iterator += 1

    result_string: str = ""
    indexer: int = 0

    while indexer < len(transformed_groups):
        result_string += transformed_groups[indexer]
        indexer += 1

    return result_string


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))