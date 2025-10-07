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
    split_numbers = [num for num in numbers.split(' ') if num != '']
    sorted_list = []
    while split_numbers:
        min_index = 0
        for i in range(1, len(split_numbers)):
            if value_map[split_numbers[i]] < value_map[split_numbers[min_index]]:
                min_index = i
        sorted_list.append(split_numbers.pop(min_index))
    result = ''
    for i, num in enumerate(sorted_list):
        if i > 0:
            result += ' '
        result += num
    return result