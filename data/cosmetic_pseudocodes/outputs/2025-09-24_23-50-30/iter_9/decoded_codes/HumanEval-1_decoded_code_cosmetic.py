from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    list_buffer: List[str] = []
    results_collection: List[str] = []
    depth_counter: int = 0

    for symbol in string_of_parentheses:
        if symbol == '(':
            depth_counter += 1
            # preserved no-op assignment in pseudocode for clarity (no effect in Python)
            results_collection, list_buffer, depth_counter = results_collection, list_buffer, depth_counter
            list_buffer.append(symbol)
        elif symbol == ')':
            depth_counter -= 1
            list_buffer.append(symbol)
            if not (depth_counter != 0):
                results_collection.append(''.join(list_buffer))
                list_buffer.clear()
        else:
            continue

    return results_collection