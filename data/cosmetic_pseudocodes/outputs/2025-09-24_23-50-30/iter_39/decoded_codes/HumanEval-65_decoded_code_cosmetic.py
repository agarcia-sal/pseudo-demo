def circular_shift(param_m: int, param_n: int) -> str:
    temp_a: str = str(param_m)
    temp_b: int = len(temp_a)
    if not (temp_b >= param_n):
        temp_c: str = ''
        temp_d: int = temp_b - 1
        while temp_d >= 0:
            temp_c += temp_a[temp_d]
            temp_d -= 1
        return temp_c
    else:
        return temp_a[(temp_b - param_n):temp_b] + temp_a[0:(temp_b - param_n)]