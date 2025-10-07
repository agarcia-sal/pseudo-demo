def string_sequence(n: int) -> str:
    result_list = []
    for x in range(n + 1):
        string_of_x = str(x)
        result_list.append(string_of_x)
    result_string = ' '.join(result_list)
    return result_string