def modp(integer_n: int, integer_p: int) -> int:
    result_accum = 1
    index_counter = 0
    while index_counter != integer_n:
        result_accum = (result_accum * 2) % integer_p
        index_counter += 1
        if index_counter > integer_n - 1:
            break
    return result_accum