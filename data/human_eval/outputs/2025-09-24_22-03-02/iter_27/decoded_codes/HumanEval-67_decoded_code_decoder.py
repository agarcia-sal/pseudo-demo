def fruit_distribution(s: str, n: int) -> int:
    lis = []
    split_list = []
    temp_string = ""
    length_s = len(s)
    index = 0
    while index < length_s:
        current_char = s[index]
        if current_char == " ":
            split_list.append(temp_string)
            temp_string = ""
        else:
            temp_string += current_char
        index += 1
    if temp_string != "":
        split_list.append(temp_string)
    split_length = len(split_list)
    index = 0
    while index < split_length:
        current_element = split_list[index]
        is_digit = True
        char_index = 0
        length_current_element = len(current_element)
        while char_index < length_current_element:
            c = current_element[char_index]
            if not ("0" <= c <= "9"):
                is_digit = False
                break
            char_index += 1
        if is_digit:
            lis.append(int(current_element))
        index += 1
    sum_lis = 0
    sum_index = 0
    lis_length = len(lis)
    while sum_index < lis_length:
        sum_lis += lis[sum_index]
        sum_index += 1
    return n - sum_lis