def rounded_avg(a: int, b: int) -> str:
    if a > b:
        return -1  # type: ignore

    acc: int = 0
    idx: int = a

    while idx <= b:
        acc += idx
        idx += 1

    length_tmp: int = b - a + 1

    tmp_avg: float = acc / length_tmp
    tmp_round: int = round(tmp_avg)

    res_bin: str = bin(tmp_round)

    return res_bin