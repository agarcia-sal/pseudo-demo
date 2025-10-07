from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def recurse_chars(index: int, curr_depth: int, max_depth: int) -> int:
            if index >= len(group_string):
                return max_depth

            char = group_string[index]
            if char == '(':
                updated_depth = curr_depth + 1
                updated_max = max(updated_depth, max_depth)
                return recurse_chars(index + 1, updated_depth, updated_max)
            if char == ')':
                return recurse_chars(index + 1, curr_depth - 1, max_depth)
            # If other characters appear (though not expected), just continue
            return recurse_chars(index + 1, curr_depth, max_depth)

        return recurse_chars(0, 0, 0)

    tokens_collection: List[str] = []
    start_idx = 0
    length_str = len(parentheses_string)

    while start_idx < length_str:
        while start_idx < length_str and parentheses_string[start_idx] == ' ':
            start_idx += 1

        end_idx = start_idx
        while end_idx < length_str and parentheses_string[end_idx] != ' ':
            end_idx += 1

        if end_idx > start_idx:
            token = parentheses_string[start_idx:end_idx]
            tokens_collection.append(token)

        start_idx = end_idx + 1

    results_array: List[int] = [parse_paren_group(token) for token in tokens_collection]

    return results_array