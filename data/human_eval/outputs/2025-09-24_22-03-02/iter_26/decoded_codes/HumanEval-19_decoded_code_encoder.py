def sort_numbers(numbers: str) -> str:
    value_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    splitted_list = numbers.split(' ')
    filtered_list = [e for e in splitted_list if e != '']
    sorted_list = []
    temp_list = filtered_list
    while temp_list:
        min_element = temp_list[0]
        for current_element in temp_list[1:]:
            if value_map[current_element] < value_map[min_element]:
                min_element = current_element
        sorted_list.append(min_element)
        temp_list = [e for e in temp_list if e != min_element]
    result_string = ' '.join(sorted_list)
    return result_string