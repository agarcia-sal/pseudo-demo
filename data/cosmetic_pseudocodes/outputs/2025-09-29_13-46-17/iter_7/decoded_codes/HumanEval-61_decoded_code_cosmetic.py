from typing import Callable

def correct_bracketing(string_of_brackets: str) -> bool:
    def helper(idx: int, net: int) -> bool:
        if idx >= len(string_of_brackets):
            return net == 0
        current_char: str = string_of_brackets[idx]
        adjustment: int = 1 if current_char == "(" else -1
        updated_net: int = net + adjustment
        if updated_net < 0:
            return False
        return helper(idx + 1, updated_net)
    return helper(0, 0)