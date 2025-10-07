from typing import List


def anti_shuffle(source_text: str) -> str:
    tokens: List[str] = source_text.split(" ")
    ordered_tokens: List[str] = []
    idx: int = 0
    while idx < len(tokens):
        element: str = tokens[idx]
        chars: List[str] = []
        pos: int = 0
        while pos < len(element):
            chars.append(element[pos])
            pos += 1
        asc_chars: List[str] = sorted(chars)
        rebuilt: str = ""
        for ch in asc_chars:
            rebuilt += ch
        ordered_tokens.append(rebuilt)
        idx += 1
    final_text: str = ""
    for enum_index in range(len(ordered_tokens)):
        final_text += ordered_tokens[enum_index]
        if enum_index < len(ordered_tokens) - 1:
            final_text += " "
    return final_text