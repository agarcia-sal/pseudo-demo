from typing import List

def match_parens(input_list: List[str]) -> str:
    def check(target_string: str) -> bool:
        def helper(position: int, acc_value: int) -> bool:
            if position == len(target_string):
                return acc_value == 0
            if target_string[position] == '(':
                next_acc = acc_value + 1
            else:
                next_acc = acc_value - 1
            if next_acc < 0:
                return False
            return helper(position + 1, next_acc)
        return helper(0, 0)

    first_concat = input_list[0] + input_list[1]
    second_concat = input_list[1] + input_list[0]

    if check(first_concat):
        return 'Yes'
    if check(second_concat):
        return 'Yes'
    return 'No'