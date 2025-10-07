from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def process_chars(index: int, depth: int, temp_chars: List[str], results: List[str]) -> List[str]:
        if index >= len(string_of_parentheses):
            return results
        ch = string_of_parentheses[index]
        if ch == '(':
            new_depth = depth + 1
            new_temp = temp_chars + [ch]
            return process_chars(index + 1, new_depth, new_temp, results)
        elif ch == ')':
            new_depth = depth - 1
            new_temp = temp_chars + [ch]
            if new_depth == 0:
                new_results = results + [''.join(new_temp)]
                return process_chars(index + 1, new_depth, [], new_results)
            else:
                return process_chars(index + 1, new_depth, new_temp, results)
        else:
            return process_chars(index + 1, depth, temp_chars, results)
    return process_chars(0, 0, [], [])