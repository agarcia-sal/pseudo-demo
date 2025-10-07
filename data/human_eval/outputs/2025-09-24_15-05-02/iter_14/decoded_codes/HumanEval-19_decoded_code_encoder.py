def sort_numbers(numbers):
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
    number_list = [x for x in numbers.split(' ') if x]
    sorted_list = sorted(number_list, key=lambda element: value_map[element])
    result = ' '.join(sorted_list)
    return result