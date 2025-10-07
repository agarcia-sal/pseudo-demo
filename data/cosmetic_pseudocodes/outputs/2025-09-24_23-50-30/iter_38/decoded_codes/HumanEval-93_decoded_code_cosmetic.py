from typing import Dict


def encode(data: str) -> str:
    vowels_set: str = "aeiouAEIOU"
    vowels_map: Dict[str, str] = {key: chr(ord(key) + 2) for key in vowels_set}
    modified: str = data.swapcase()
    handle: list[str] = []
    for ch in modified:
        if ch in vowels_set:
            handle.append(vowels_map[ch])
        else:
            handle.append(ch)
    return "".join(handle)