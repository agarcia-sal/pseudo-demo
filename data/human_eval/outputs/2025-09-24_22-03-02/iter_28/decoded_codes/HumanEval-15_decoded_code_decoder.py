def string_sequence(n: int) -> str:
    result_list = [""]
    index = 0
    while index <= n:
        result_list.append(str(index))
        index += 1
    result_string = ""
    index = 0
    while index < len(result_list):
        if index == 0:
            result_string = result_list[index]
        else:
            result_string += " " + result_list[index]
        index += 1
    return result_string