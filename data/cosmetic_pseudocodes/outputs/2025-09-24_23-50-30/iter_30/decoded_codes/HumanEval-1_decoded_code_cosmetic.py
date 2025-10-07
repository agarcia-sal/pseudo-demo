from typing import List


def separate_paren_groups(parentheses_seq: str) -> List[str]:
    results: List[str] = []
    buffer: List[str] = []
    depth_counter: int = 0

    def process_index(idx: int) -> None:
        nonlocal depth_counter
        if idx >= len(parentheses_seq):
            return
        ch: str = parentheses_seq[idx]
        if ch == '(':
            depth_counter += 1
            buffer.append(ch)
        elif ch == ')':
            depth_counter -= 1
            buffer.append(ch)
            if depth_counter == 0:
                results.append(''.join(buffer))
                buffer.clear()
        process_index(idx + 1)

    process_index(0)
    return results