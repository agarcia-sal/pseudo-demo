def string_sequence(n: int) -> str:
    string_list = [""]
    for index in range(n + 1):
        number_string = str(index)
        string_list.append(number_string)
    result_string = ""
    for index in range(len(string_list)):
        if index == 0:
            result_string = string_list[index]
        else:
            result_string = result_string + " " + string_list[index]
    return result_string