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
    filtered_list = []
    for x in numbers.split(' '):
        if x != '':
            filtered_list.append(x)
    sorted_list = sorted(filtered_list, key=lambda x: value_map[x])
    result = ' '.join(sorted_list)
    return result