from typing import Union


def iscube(integer_value: int) -> bool:
    temp_var1: int = integer_value
    if temp_var1 < 0:
        temp_var1 = -temp_var1

    temp_var2: int = temp_var1
    temp_var3: int = 0
    error_flag: bool = False  # unused but preserved per pseudocode

    temp_var4: float = 1.0 / 3.0
    temp_var5: float = temp_var2 ** temp_var4
    temp_var3 = round(temp_var5)

    temp_var6: int = temp_var3 * temp_var3 * temp_var3
    if temp_var6 == temp_var2:
        return True
    else:
        return False