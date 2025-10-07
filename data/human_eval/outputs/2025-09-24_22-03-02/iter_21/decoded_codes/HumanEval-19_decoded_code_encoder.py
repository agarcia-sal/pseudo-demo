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
    def key_function(x: str) -> int:
        return value_map[x]
    sorted_numbers = sorted(filtered_numbers, key=key_function)
    result_string = ''
    for index in range(len(sorted_numbers)):
        result_string += sorted_numbers[index]
        if index != len(sorted_numbers) - 1:
            result_string += ' '
    return result_string