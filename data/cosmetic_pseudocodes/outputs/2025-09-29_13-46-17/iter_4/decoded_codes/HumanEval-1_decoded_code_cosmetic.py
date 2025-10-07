from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def helper(index_iter: int, depth_counter: int, acc_chars: List[str], acc_results: List[str]) -> List[str]:
        if index_iter >= len(string_of_parentheses):
            return acc_results
        current_char = string_of_parentheses[index_iter]
        if current_char not in ('(', ')'):
            return helper(index_iter + 1, depth_counter, acc_chars, acc_results)
        if current_char == '(':
            new_depth = depth_counter + 1
            new_acc_chars = acc_chars + [current_char]
            return helper(index_iter + 1, new_depth, new_acc_chars, acc_results)
        # current_char == ')'
        new_depth = depth_counter - 1
        new_acc_chars = acc_chars + [current_char]
        if new_depth == 0:
            new_acc_results = acc_results + [''.join(new_acc_chars)]
            return helper(index_iter + 1, new_depth, [], new_acc_results)
        return helper(index_iter + 1, new_depth, new_acc_chars, acc_results)

    return helper(0, 0, [], [])