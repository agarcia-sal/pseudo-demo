def sort_numbers(numbers: str) -> str:
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    split_numbers = []
    temp_list = []
    index_split = 0
    while index_split < len(numbers):
        current_char = numbers[index_split]
        if current_char == ' ':
            split_numbers.append(''.join(temp_list))
            temp_list = []
        else:
            temp_list.append(current_char)
        index_split += 1
    if len(temp_list) > 0:
        split_numbers.append(''.join(temp_list))
    filtered_numbers = []
    index_filtered = 0
    while index_filtered < len(split_numbers):
        if split_numbers[index_filtered] != '':
            filtered_numbers.append(split_numbers[index_filtered])
        index_filtered += 1
    index_outer = 0
    while index_outer < len(filtered_numbers) - 1:
        index_inner = index_outer + 1
        while index_inner < len(filtered_numbers):
            if value_map[filtered_numbers[index_outer]] > value_map[filtered_numbers[index_inner]]:
                temp = filtered_numbers[index_outer]
                filtered_numbers[index_outer] = filtered_numbers[index_inner]
                filtered_numbers[index_inner] = temp
            index_inner += 1
        index_outer += 1
    result_string = ''
    index_result = 0
    while index_result < len(filtered_numbers):
        if index_result == 0:
            result_string = filtered_numbers[index_result]
        else:
            result_string = result_string + ' ' + filtered_numbers[index_result]
        index_result += 1
    return result_string