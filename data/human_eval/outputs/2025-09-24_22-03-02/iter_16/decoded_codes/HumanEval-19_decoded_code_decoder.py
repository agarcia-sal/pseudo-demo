from math import inf

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
    filtered_numbers = [x for x in split_numbers if x != '']
    sorted_numbers = []
    while filtered_numbers:
        smallest_value = inf
        smallest_element = ''
        for element in filtered_numbers:
            if value_map[element] < smallest_value:
                smallest_value = value_map[element]
                smallest_element = element
        sorted_numbers.append(smallest_element)
        filtered_numbers.remove(smallest_element)
    result = ' '.join(sorted_numbers)
    return result