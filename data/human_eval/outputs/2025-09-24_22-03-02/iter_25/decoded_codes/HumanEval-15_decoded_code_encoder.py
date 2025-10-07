def string_sequence(n: int) -> str:
    result_list = [""]
    i = 0
    while i <= n:
        result_list.append(str(i))
        i += 1
    result_string = ""
    index = 0
    length = len(result_list)
    while index < length:
        result_string += result_list[index]
        if index < length - 1:
            result_string += " "
        index += 1
    return result_string