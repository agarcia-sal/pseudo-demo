def is_happy(str_param: str) -> bool:
    length = len(str_param)
    if length < 3:
        return False
    pos_counter = 0
    while pos_counter <= length - 3:
        if str_param[pos_counter] == str_param[pos_counter + 1]:
            return False
        if str_param[pos_counter + 1] == str_param[pos_counter + 2]:
            return False
        if str_param[pos_counter] == str_param[pos_counter + 2]:
            return False
        pos_counter += 1
    return True