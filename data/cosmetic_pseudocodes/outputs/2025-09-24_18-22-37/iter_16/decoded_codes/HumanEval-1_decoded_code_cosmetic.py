from typing import List

def separate_paren_groups(input_sequence: str) -> List[str]:
    collected_substrings: List[str] = []
    active_chars: List[str] = []
    depth_counter: int = 0

    position: int = 0
    while position < len(input_sequence):
        current_symbol: str = input_sequence[position]

        if current_symbol == '(':
            depth_counter += 1
            active_chars.append(current_symbol)

        else:
            if current_symbol == ')':
                depth_counter -= 1
                active_chars.append(current_symbol)

                if depth_counter == 0:
                    composed_string = ''.join(active_chars)
                    collected_substrings.append(composed_string)
                    active_chars.clear()

        position += 1

    return collected_substrings