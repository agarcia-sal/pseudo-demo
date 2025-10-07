from math import exp, log


def iscube(integer_value: int) -> bool:
    temp_var1: int = integer_value
    if temp_var1 < 0:
        temp_var1 = -temp_var1

    temp_var2: int = round(exp(log(temp_var1) / 3))
    temp_var3: int = temp_var2 * temp_var2 * temp_var2

    if temp_var3 == temp_var1:
        return True
    else:
        return False