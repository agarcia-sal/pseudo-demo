from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collected_segments: List[str] = []
    segment_accumulator: List[str] = []
    depth_counter: int = 0

    index_tracker: int = 0
    while index_tracker < len(string_of_parentheses):
        current_element: str = string_of_parentheses[index_tracker]

        if current_element == '(':
            depth_counter += 1
            segment_accumulator.append(current_element)
        elif current_element == ')':
            depth_counter -= 1
            segment_accumulator.append(current_element)
            if depth_counter == 0:
                joined_segment = "".join(segment_accumulator)
                collected_segments.append(joined_segment)
                segment_accumulator = []
        else:
            # No operation for characters other than '(' or ')'
            pass

        index_tracker += 1

    return collected_segments