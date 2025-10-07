def fruit_distribution(s, n):
    lis = []
    split_list = []
    temp_string = ''
    length_of_s = len(s)
    index = 0
    while index < length_of_s:
        current_char = s[index]
        if current_char == ' ':
            split_list.append(temp_string)
            temp_string = ''
        else:
            temp_string += current_char
        index += 1
    if temp_string != '':
        split_list.append(temp_string)

    index = 0
    length_of_split_list = len(split_list)
    while index < length_of_split_list:
        element = split_list[index]
        is_digit = True
        digit_index = 0
        length_of_element = len(element)
        while digit_index < length_of_element:
            char = element[digit_index]
            if not ('0' <= char <= '9'):
                is_digit = False
                break
            digit_index += 1
        if is_digit:
            lis.append(int(element))
        index += 1

    sum_lis = 0
    index = 0
    length_of_lis = len(lis)
    while index < length_of_lis:
        sum_lis += lis[index]
        index += 1

    result = n - sum_lis
    return result