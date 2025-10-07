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
    split_list = []
    index = 0
    while index < len(numbers):
        current_char = numbers[index]
        if current_char == ' ':
            split_list.append('')
            index += 1
        else:
            if len(split_list) == 0:
                split_list.append('')
            last_index = len(split_list) - 1
            last_string = split_list[last_index]
            updated_string = last_string + current_char
            split_list[last_index] = updated_string
            index += 1
    filtered_list = []
    index = 0
    while index < len(split_list):
        if split_list[index] != '':
            filtered_list.append(split_list[index])
        index += 1
    sorted_list = []
    while len(sorted_list) < len(filtered_list):
        min_index = 0
        min_value = filtered_list[0]
        i = 1
        while i < len(filtered_list):
            current_value = filtered_list[i]
            if value_map[current_value] < value_map[min_value]:
                min_index = i
                min_value = current_value
            i += 1
        sorted_list.append(min_value)
        filtered_list.pop(min_index)
    result = ''
    j = 0
    while j < len(sorted_list):
        if j > 0:
            result += ' '
        result += sorted_list[j]
        j += 1
    return result