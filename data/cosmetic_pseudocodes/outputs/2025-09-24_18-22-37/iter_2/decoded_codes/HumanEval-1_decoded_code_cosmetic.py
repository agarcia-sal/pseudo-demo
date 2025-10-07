from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    output_segments: List[str] = []
    segment_buffer: List[str] = []
    depth_counter: int = 0

    for ch in string_of_parentheses:
        if ch == '(':
            depth_counter += 1
            segment_buffer.append(ch)
        elif ch == ')':
            segment_buffer.append(ch)
            depth_counter -= 1
            if depth_counter == 0:
                output_segments.append(''.join(segment_buffer))
                segment_buffer.clear()
        else:
            continue

    return output_segments