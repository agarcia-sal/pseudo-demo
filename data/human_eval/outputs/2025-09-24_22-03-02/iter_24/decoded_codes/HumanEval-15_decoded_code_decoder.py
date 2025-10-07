def string_sequence(n: int) -> str:
    result_list = ['']
    for index in range(n + 1):
        result_list.append(str(index))
    result_string = ''
    for index in range(len(result_list)):
        if index > 0:
            result_string = result_string + ' ' + result_list[index]
        else:
            result_string = result_list[index]
    return result_string