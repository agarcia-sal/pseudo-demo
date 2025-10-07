def string_sequence(n: int) -> str:
    result_list = ['']
    i = 0
    while i <= n:
        result_list.append(str(i))
        i += 1
    result_string = ''
    j = 0
    while j < len(result_list):
        result_string += result_list[j]
        if j < len(result_list) - 1:
            result_string += ' '
        j += 1
    return result_string