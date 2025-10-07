from typing import List

def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    total_groups: int = (len(input_string) + 2) // 3
    for i in range(total_groups):
        start_index: int = 3 * i
        end_index: int = min(3 * i + 3, len(input_string))
        groups.append(input_string[start_index:end_index])

    for idx, group in enumerate(groups):
        if len(group) == 3:
            # Rotate characters: move first character to the end
            groups[idx] = group[1:] + group[0]

    return ''.join(groups)

def decode_cyclic(encoded_string: str) -> str:
    # Decoding is encoding applied twice
    return encode_cyclic(encode_cyclic(encoded_string))