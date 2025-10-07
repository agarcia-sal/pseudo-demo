def sort_numbers(numbers_string):
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
    split_numbers = [num for num in numbers_string.split(' ') if num]
    sorted_numbers = []
    while len(split_numbers) > 0:
        min_index = 0
        for i in range(1, len(split_numbers)):
            if value_map[split_numbers[i]] < value_map[split_numbers[min_index]]:
                min_index = i
        sorted_numbers.append(split_numbers[min_index])
        split_numbers.pop(min_index)
    result_string = ' '.join(sorted_numbers)
    return result_string