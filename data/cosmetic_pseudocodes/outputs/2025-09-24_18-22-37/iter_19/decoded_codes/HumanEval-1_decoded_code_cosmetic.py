from typing import List


def separate_paren_groups(input_sequence: str) -> List[str]:
    collected_results: List[str] = []
    collector_chars: List[str] = []
    depth_counter: int = 0

    iterator_index: int = 0
    length: int = len(input_sequence)
    while iterator_index < length:
        current_symbol: str = input_sequence[iterator_index]

        if current_symbol == '(':
            depth_counter += 1
            collector_chars.append(current_symbol)
        elif current_symbol == ')':
            depth_counter -= 1
            collector_chars.append(current_symbol)

            if depth_counter == 0:
                joined_string = ''.join(collector_chars)
                collected_results.append(joined_string)
                collector_chars = []

        iterator_index += 1

    return collected_results