from typing import List

def words_string(input_string: str) -> List[str]:
    accumulator: List[str] = []

    def helper(index: int) -> None:
        if index >= len(input_string):
            return
        current_char = input_string[index]
        if current_char != ',':
            accumulator.append(current_char)
        else:
            accumulator.append(' ')
        helper(index + 1)

    if len(input_string) == 0:
        return []

    helper(0)

    return ''.join(accumulator).split(' ')