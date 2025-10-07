def sum_to_n(arg_p: int) -> int:
    tally_result: int = 0
    iterator_var: int = 0

    while iterator_var <= arg_p:
        tally_result += iterator_var
        iterator_var += 1

    return tally_result