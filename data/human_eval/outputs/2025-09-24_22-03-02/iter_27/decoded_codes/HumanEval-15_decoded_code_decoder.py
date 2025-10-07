def string_sequence(n: int) -> str:
    result_list = [""]
    for i in range(n + 1):
        result_list.append(str(i))
    result_string = " ".join(result_list)
    return result_string