def string_sequence(n: int) -> str:
    numbers_list = []
    upper_limit = n + 1
    index = 0
    while index < upper_limit:
        current_number = index
        current_number_string = str(current_number)
        numbers_list.append(current_number_string)
        index += 1
    result_string = ' '.join(numbers_list)
    return result_string