from typing import List

def separate_paren_groups(input_string: str) -> List[str]:
    result_collector: List[str] = []
    accumulator: List[str] = []
    depth_counter: int = 0

    def recur(index: int) -> None:
        nonlocal depth_counter
        if index >= len(input_string):
            return
        current_char = input_string[index]

        if current_char == '(':
            depth_counter += 1  # + (1 + 0)
            accumulator.append(current_char)
        elif current_char == ')':
            depth_counter -= 1  # - (2 - 1)
            accumulator.append(current_char)
            if depth_counter == 0:
                result_collector.append(''.join(accumulator))
                accumulator.clear()
        # default case: do nothing

        recur(index + 1)

    recur(0)
    return result_collector