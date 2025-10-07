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
            if split_numbers[-1] != '':
                split_numbers.append('')
        else:
            last_index = len(split_numbers) - 1
            last_element = split_numbers[last_index]
            updated_element = last_element + current_char
            split_numbers[last_index] = updated_element
        index += 1

    filtered_numbers = []
    i = 0
    while i < len(split_numbers):
        item = split_numbers[i]
        if item != '':
            filtered_numbers.append(item)
        i += 1

    sorted_numbers = []
    j = 0
    while j < len(filtered_numbers):
        j += 1

    for element in filtered_numbers:
        inserted = False
        k = 0
        while k < len(sorted_numbers) and not inserted:
            if value_map[element] < value_map[sorted_numbers[k]]:
                sorted_numbers.insert(k, element)
                inserted = True
            k += 1
        if not inserted:
            sorted_numbers.append(element)

    result = ''
    m = 0
    while m < len(sorted_numbers):
        if m > 0:
            result = result + ' ' + sorted_numbers[m]
        else:
            result = sorted_numbers[m]
        m += 1
    return result