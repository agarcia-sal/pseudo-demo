def string_sequence(n: int) -> str:
    result_list = ['']
    for i in range(n + 1):
        string_element = str(i)
        result_list.append(string_element)
    result_string = ''
    for j in range(len(result_list)):
        if j == 0:
            result_string = result_list[j]
        else:
            result_string = result_string + ' ' + result_list[j]
    return result_string