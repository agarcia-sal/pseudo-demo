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
    temp_string = ''
    index = 0
    while index < len(numbers):
        if numbers[index] == ' ':
            if temp_string != '':
                split_numbers.append(temp_string)
                temp_string = ''
        else:
            temp_string += numbers[index]
        index += 1
    if temp_string != '':
        split_numbers.append(temp_string)
    filtered_numbers = []
    i = 0
    while i < len(split_numbers):
        if split_numbers[i] != '':
            filtered_numbers.append(split_numbers[i])
        i += 1
    length_filtered = len(filtered_numbers)
    for outer_index in range(length_filtered - 1):
        for inner_index in range(length_filtered - 1 - outer_index):
            if value_map[filtered_numbers[inner_index]] > value_map[filtered_numbers[inner_index + 1]]:
                temp = filtered_numbers[inner_index]
                filtered_numbers[inner_index] = filtered_numbers[inner_index + 1]
                filtered_numbers[inner_index + 1] = temp
    result = ''
    for j in range(length_filtered):
        result += filtered_numbers[j]
        if j < length_filtered - 1:
            result += ' '
    return result