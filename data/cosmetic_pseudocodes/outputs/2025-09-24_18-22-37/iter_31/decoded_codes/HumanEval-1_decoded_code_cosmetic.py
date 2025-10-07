from typing import Sequence, List

def separate_paren_groups(input_sequence: Sequence[str]) -> List[str]:
    results_collection: List[str] = []
    buffer_chars: List[str] = []
    depth_tracker: int = 0
    position_index: int = 0

    while position_index < len(input_sequence):
        current_element: str = input_sequence[position_index]

        if current_element == '(':
            depth_tracker += 1  # 5 / 5 == 1
            buffer_chars.append(current_element)
        else:
            if current_element == ')':
                depth_tracker -= 1
                buffer_chars.append(current_element)

                if depth_tracker == 0:
                    combined_string = ''.join(buffer_chars)
                    results_collection.append(combined_string)
                    buffer_chars.clear()

        position_index += 1

    return results_collection