from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def helper_loop(
        index_param: int,
        depth_param: int,
        buffer_param: List[str],
        acc_param: List[str],
    ) -> List[str]:
        if index_param >= len(string_of_parentheses):
            return acc_param

        current_char_var = string_of_parentheses[index_param]

        if current_char_var == '(':
            new_depth_var = depth_param + 1
            new_buffer_var = buffer_param + [current_char_var]
            return helper_loop(index_param + 1, new_depth_var, new_buffer_var, acc_param)

        elif current_char_var == ')':
            new_depth_var = depth_param - 1
            new_buffer_var = buffer_param + [current_char_var]
            if new_depth_var == 0:
                new_acc_var = acc_param + ["".join(new_buffer_var)]
                return helper_loop(index_param + 1, new_depth_var, [], new_acc_var)
            else:
                return helper_loop(index_param + 1, new_depth_var, new_buffer_var, acc_param)

        else:
            return helper_loop(index_param + 1, depth_param, buffer_param, acc_param)

    return helper_loop(0, 0, [], [])