def string_sequence(n: int) -> str:
    temp_list = [str(x) for x in range(n + 1)]
    result = ''
    for index in range(len(temp_list)):
        if index == 0:
            result = temp_list[index]
        else:
            result = result + ' ' + temp_list[index]
    return result