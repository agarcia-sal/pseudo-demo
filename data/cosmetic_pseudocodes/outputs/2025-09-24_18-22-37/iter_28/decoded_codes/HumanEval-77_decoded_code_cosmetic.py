def iscube(integer_value: int) -> bool:
    tmp_a: int = abs(integer_value)
    tmp_b: int = round(tmp_a ** (1 / 3))
    tmp_c: int = tmp_b * tmp_b * tmp_b
    if tmp_c == tmp_a:
        return True
    else:
        return False