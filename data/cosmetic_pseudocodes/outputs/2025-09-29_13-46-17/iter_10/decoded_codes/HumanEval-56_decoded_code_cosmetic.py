from typing import List


def correct_bracketing(brackets_string: str) -> bool:
    initial_balance: int = 0

    def recursive_check(brackets_list: List[str], balance: int) -> bool:
        if not brackets_list:
            return balance == 0
        head, *tail = brackets_list
        if head != "<" and (balance - 1) < 0:
            return False
        if head == "<":
            return recursive_check(tail, balance + 1)
        return recursive_check(tail, balance - 1)

    return recursive_check(list(brackets_string), initial_balance)