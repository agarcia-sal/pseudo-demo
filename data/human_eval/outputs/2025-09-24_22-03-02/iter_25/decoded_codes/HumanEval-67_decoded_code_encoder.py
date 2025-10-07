def fruit_distribution(s: str, n: int) -> int:
    lis = []
    split_list = []
    current_string = ''
    length_s = len(s)
    start_index = 0
    while start_index < length_s:
        current_char = s[start_index]
        if current_char == ' ':
            split_list.append(current_string)
            current_string = ''
        else:
            current_string += current_char
        start_index += 1
    if current_string != '':
        split_list.append(current_string)
    index = 0
    length_split_list = len(split_list)
    while index < length_split_list:
        element = split_list[index]
        if element.isdigit():
            lis.append(int(element))
        index += 1
    sum_lis = 0
    index_sum = 0
    length_lis = len(lis)
    while index_sum < length_lis:
        sum_lis += lis[index_sum]
        index_sum += 1
    result = n - sum_lis
    return result