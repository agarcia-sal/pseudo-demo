from typing import List


def is_nested(text: str) -> bool:
    start_positions: List[int] = []
    end_positions: List[int] = []
    ptr: int = 0
    text_length: int = len(text)
    while ptr < text_length:
        ch: str = text[ptr]
        if ch == '[':
            start_positions.append(ptr)
        else:
            end_positions.append(ptr)
        ptr += 1
    end_positions.reverse()

    matched_count: int = 0
    end_ptr: int = 0
    end_len: int = len(end_positions)
    for element in start_positions:
        if end_ptr < end_len and element < end_positions[end_ptr]:
            matched_count += 1
            end_ptr += 1
    return matched_count >= 2