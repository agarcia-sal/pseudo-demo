from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def process_chars(
        chars: List[str],
        depth: int,
        acc_string: str,
        acc_results: List[str],
        pos: int,
    ) -> List[str]:
        if pos == len(chars):
            return acc_results

        current_char = chars[pos]

        if current_char == "(":
            return process_chars(chars, depth + 1, acc_string + current_char, acc_results, pos + 1)
        elif current_char == ")":
            new_depth = depth - 1
            new_acc_string = acc_string + current_char

            if new_depth == 0:
                return process_chars(chars, new_depth, "", acc_results + [new_acc_string], pos + 1)
            else:
                return process_chars(chars, new_depth, new_acc_string, acc_results, pos + 1)
        else:
            return process_chars(chars, depth, acc_string, acc_results, pos + 1)

    return process_chars(list(string_of_parentheses), 0, "", [], 0)