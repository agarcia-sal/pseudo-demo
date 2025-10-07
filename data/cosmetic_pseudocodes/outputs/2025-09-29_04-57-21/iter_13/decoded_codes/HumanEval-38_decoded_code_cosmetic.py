from typing import List


def encode_cyclic(input_string: str) -> str:
    collected_groups: List[str] = []

    def collect_groups(idx: int, limit: int) -> None:
        if idx > limit:
            return
        start_pos = idx * 3
        end_pos = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        collected = input_string[start_pos:end_pos]
        collected_groups.append(collected)
        collect_groups(idx + 1, limit)

    max_index = ((len(input_string) + 2) // 3) - 1
    collect_groups(0, max_index)

    transformed_groups: List[str] = []
    i = 0
    while i < len(collected_groups):
        segment = collected_groups[i]
        if len(segment) != 3:
            transformed_groups.append(segment)
            i += 1
            continue
        # Rotate first character to the end
        transformed_groups.append(segment[1:] + segment[0])
        i += 1

    output = ''.join(transformed_groups)
    return output


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))