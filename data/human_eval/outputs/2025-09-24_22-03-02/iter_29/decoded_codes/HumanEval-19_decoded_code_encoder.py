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
    split_numbers = numbers.split(' ')
    filtered_numbers = [num for num in split_numbers if num != '']
    for i in range(len(filtered_numbers) - 1):
        for j in range(len(filtered_numbers) - 1 - i):
            left_value = value_map[filtered_numbers[j]]
            right_value = value_map[filtered_numbers[j + 1]]
            if left_value > right_value:
                filtered_numbers[j], filtered_numbers[j + 1] = filtered_numbers[j + 1], filtered_numbers[j]
    result_string = ''
    for k in range(len(filtered_numbers)):
        if k > 0:
            result_string += ' '
        result_string += filtered_numbers[k]
    return result_string