def string_sequence(n: int) -> str:
    result_list = []
    for x in range(0, n + 1):
        result_list.append(str(x))
    return ' '.join(result_list)