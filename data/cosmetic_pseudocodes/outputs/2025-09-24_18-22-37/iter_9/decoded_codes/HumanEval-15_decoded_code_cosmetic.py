def string_sequence(integer_coord: int) -> str:
    concat_result: str = ""
    index_var: int = 0
    while index_var <= integer_coord:
        str_temp: str = str(index_var)
        if index_var == 0:
            concat_result = str_temp
        else:
            concat_result = concat_result + " " + str_temp
        index_var += 1
    return concat_result