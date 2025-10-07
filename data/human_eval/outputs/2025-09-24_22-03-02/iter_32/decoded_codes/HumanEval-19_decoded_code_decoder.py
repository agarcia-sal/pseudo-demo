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
    sorted_numbers = []
    used_indices = []
    for _ in range(len(filtered_numbers)):
        min_value = float('inf')
        min_index = -1
        for j in range(len(filtered_numbers)):
            if j not in used_indices:
                current_value = value_map.get(filtered_numbers[j])
                if current_value is not None and current_value < min_value:
                    min_value = current_value
                    min_index = j
        if min_index == -1:
            break
        sorted_numbers.append(filtered_numbers[min_index])
        used_indices.append(min_index)
    result = ''
    for k in range(len(sorted_numbers) - 1):
        result += sorted_numbers[k] + ' '
    if len(sorted_numbers) > 0:
        result += sorted_numbers[-1]
    return result