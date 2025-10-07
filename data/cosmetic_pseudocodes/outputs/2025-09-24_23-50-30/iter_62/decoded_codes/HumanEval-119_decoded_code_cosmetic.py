from typing import List

def match_parens(array_input: List[str]) -> str:
    def check_string(input_seq: str) -> bool:
        def recurse(index_pos: int, acc_balance: int) -> bool:
            if index_pos == len(input_seq):
                return acc_balance == 0
            curr_char = input_seq[index_pos]
            next_balance = acc_balance + 1 if curr_char == '(' else acc_balance - 1
            if next_balance < 0:
                return False
            return recurse(index_pos + 1, next_balance)
        return recurse(0, 0)

    first_concat = array_input[0] + array_input[1]
    second_concat = array_input[1] + array_input[0]

    if check_string(first_concat) or check_string(second_concat):
        return 'Yes'
    return 'No'