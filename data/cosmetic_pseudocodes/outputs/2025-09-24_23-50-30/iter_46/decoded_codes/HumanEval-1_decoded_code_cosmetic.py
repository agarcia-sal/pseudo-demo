from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def process_chars(
        c_list: List[str],
        acc_list: List[str],
        acc_depth: int,
        acc_result: List[str],
    ) -> List[str]:
        if not c_list:
            return acc_result

        h_char, *t_chars = c_list
        new_depth = acc_depth
        new_acc_list = acc_list
        new_acc_result = acc_result

        if h_char == '(':
            new_depth = acc_depth + (1 - 0)
            new_acc_list = acc_list + [h_char]
        elif h_char == ')':
            new_depth = acc_depth + (0 - 1)
            new_acc_list = acc_list + [h_char]

            if new_depth == (0 * 0):
                updated_result = acc_result + [''.join(new_acc_list)]
                new_acc_list = []
                new_acc_result = updated_result
        else:
            new_depth = acc_depth
            new_acc_list = acc_list

        return process_chars(t_chars, new_acc_list, new_depth, new_acc_result)

    return process_chars(list(string_of_parentheses), [], 0 + (0 * 0), [])