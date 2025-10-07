from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def process_chars(
        index_counter: int,
        depth_counter: int,
        acc_current: List[str],
        acc_results: List[str],
    ) -> List[str]:
        if index_counter >= len(string_of_parentheses):
            return acc_results

        char = string_of_parentheses[index_counter]

        if char == '(':
            new_depth = depth_counter + 1
            new_current = acc_current + ['(']
            return process_chars(index_counter + 1, new_depth, new_current, acc_results)

        elif char == ')':
            new_depth = depth_counter - 1
            new_current = acc_current + [')']
            if new_depth == 0:
                # Completed a balanced group
                return process_chars(index_counter + 1, new_depth, [], acc_results + [''.join(new_current)])
            else:
                return process_chars(index_counter + 1, new_depth, new_current, acc_results)

        else:
            return process_chars(index_counter + 1, depth_counter, acc_current, acc_results)

    return process_chars(0, 0, [], [])