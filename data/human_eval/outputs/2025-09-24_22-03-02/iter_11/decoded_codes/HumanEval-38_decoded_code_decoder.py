from typing import List

def encode_cyclic(s: str) -> str:
    groups: List[str] = [s[3*i:min(3*i+3, len(s))] for i in range((len(s) + 2) // 3)]
    result_groups: List[str] = []
    for group in groups:
        if len(group) == 3:
            result_groups.append(group[1:] + group[0])
        else:
            result_groups.append(group)
    return ''.join(result_groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))