def circular_shift(integer_p: int, integer_q: int) -> str:
    str_rep = str(integer_p)
    if integer_q > len(str_rep):
        return str_rep[::-1]
    else:
        len_val = len(str_rep)
        return str_rep[len_val - integer_q : len_val] + str_rep[:len_val - integer_q]