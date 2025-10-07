from typing import List


def separate_paren_groups(input_sequence: str) -> List[str]:
    accumulator: List[str] = []
    buffer: List[str] = []
    depth_counter: int = 0

    def process_next(index: int) -> None:
        nonlocal depth_counter
        if index >= len(input_sequence):
            return
        current_char = input_sequence[index]
        if current_char == '(':
            depth_counter += 1
            buffer.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer.append(current_char)
            if depth_counter == 0:
                accumulator.append(''.join(buffer))
                buffer.clear()
        # else: do nothing
        process_next(index + 1)

    process_next(0)
    return accumulator