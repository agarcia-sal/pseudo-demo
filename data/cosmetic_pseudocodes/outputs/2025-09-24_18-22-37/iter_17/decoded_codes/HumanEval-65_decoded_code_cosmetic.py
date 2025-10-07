def circular_shift(num_val: int, shift_amt: int) -> str:
    str_form = str(num_val)
    str_length = len(str_form)
    if shift_amt <= str_length:
        cut_point = str_length - shift_amt
        part_after = str_form[cut_point:str_length]
        part_before = str_form[:cut_point]
        return part_after + part_before
    return str_form[::-1]