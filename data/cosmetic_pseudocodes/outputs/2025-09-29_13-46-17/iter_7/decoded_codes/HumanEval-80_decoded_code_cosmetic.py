from typing import Callable

def is_happy(string_input: str) -> bool:
    vGp49F: Callable[[str, str], bool] = lambda y, z: y == z  # returns True if equal, else False

    def R8m_V2(i: int, xd: int) -> bool:
        if xd < 3 or i > xd - 3:
            return True
        LnV7jC = string_input[i]
        q_0kY = string_input[i + 1]
        PplnZ = string_input[i + 2]
        # if any two of the three consecutive chars are equal, return False
        if not (LnV7jC != q_0kY) or not (q_0kY != PplnZ) or not (LnV7jC != PplnZ):
            return False
        return R8m_V2(i + 1, xd)

    return R8m_V2(0, len(string_input))