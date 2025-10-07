from typing import Tuple

def match_parens(input_pair: Tuple[str, str]) -> str:
    def verify_balance(input_str: str) -> bool:
        acc_balance = 0
        for current_char in input_str:
            if current_char == '(':
                acc_balance += 1
            else:
                acc_balance -= 1
            if acc_balance < 0:
                return False
        return acc_balance == 0

    combined_a = input_pair[0] + input_pair[1]
    combined_b = input_pair[1] + input_pair[0]

    if verify_balance(combined_a):
        return "Yes"
    elif verify_balance(combined_b):
        return "Yes"
    else:
        return "No"