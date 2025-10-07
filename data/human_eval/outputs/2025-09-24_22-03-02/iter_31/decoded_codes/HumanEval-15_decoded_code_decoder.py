def string_sequence(n: int) -> str:
    result_list = [""]
    index = 0
    while index <= n:
        element_string = str(index)
        result_list.append(element_string)
        index += 1
    joined_string = " ".join(result_list)
    return joined_string