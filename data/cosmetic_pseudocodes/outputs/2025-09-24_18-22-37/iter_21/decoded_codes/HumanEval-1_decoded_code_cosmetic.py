from typing import List

def separate_paren_groups(str_paren: str) -> List[str]:
    results_collection: List[str] = []
    temp_chars: List[str] = []
    depth_counter: int = 0

    idx: int = 0
    length: int = len(str_paren)
    while idx < length:
        curr_char: str = str_paren[idx]

        if curr_char == '(':
            depth_counter += 1
            temp_chars.append(curr_char)
        elif curr_char == ')':
            depth_counter -= 1
            temp_chars.append(curr_char)

            if depth_counter == 0:
                combined_str = "".join(temp_chars)
                results_collection.append(combined_str)
                temp_chars.clear()
        # do nothing for other characters

        idx += 1

    return results_collection