def string_sequence(n: int) -> str:
    result_list = []
    i = 0
    while i <= n:
        str_element = str(i)
        result_list.append(str_element)
        i += 1
    result_string = " ".join(result_list)
    return result_string