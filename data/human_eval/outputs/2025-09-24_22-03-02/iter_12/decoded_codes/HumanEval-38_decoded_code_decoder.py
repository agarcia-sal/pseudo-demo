from typing import List

def encode_cyclic(s: str) -> str:
    groups: List[str] = []
    for i in range((len(s) + 2) // 3):
        groups.append(s[3 * i:min(3 * i + 3, len(s))])
    new_groups: List[str] = []
    for group in groups:
        if len(group) == 3:
            new_groups.append(group[1:] + group[0])
        else:
            new_groups.append(group)
    result = ''.join(new_groups)
    return result

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))