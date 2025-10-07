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
    split_numbers = ['']
    index = 0
    while index < len(numbers):
        current_char = numbers[index]
        if current_char == ' ':
            split_numbers.append('')
        else:
            if len(split_numbers) == 0:
                split_numbers.append('')
            last_index = len(split_numbers) - 1
            split_numbers[last_index] = split_numbers[last_index] + current_char
        index += 1
    filtered_numbers = []
    idx = 0
    while idx < len(split_numbers):
        if split_numbers[idx] != '':
            filtered_numbers.append(split_numbers[idx])
        idx += 1
    sorted_numbers = []
    i = 0
    while i < len(filtered_numbers):
        inserted = False
        j = 0
        while j < len(sorted_numbers):
            if value_map[filtered_numbers[i]] < value_map[sorted_numbers[j]]:
                sorted_numbers.insert(j, filtered_numbers[i])
                inserted = True
                break
            j += 1
        if not inserted:
            sorted_numbers.append(filtered_numbers[i])
        i += 1
    result = ''
    k = 0
    while k < len(sorted_numbers):
        if k > 0:
            result = result + ' '
        result = result + sorted_numbers[k]
        k += 1
    return result