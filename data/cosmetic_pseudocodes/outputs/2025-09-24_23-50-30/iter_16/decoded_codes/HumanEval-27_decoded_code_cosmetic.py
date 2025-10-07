from typing import Callable

def flip_case(str_input: str) -> str:
    def switch_case(char_val: str) -> str:
        if char_val == char_val.lower():
            return char_val.upper()
        else:
            return char_val.lower()

    def process(index_acc: int, acc_str: str) -> str:
        if index_acc >= len(str_input):
            return acc_str
        else:
            return process(index_acc + 1, acc_str + switch_case(str_input[index_acc]))

    return process(0, "")