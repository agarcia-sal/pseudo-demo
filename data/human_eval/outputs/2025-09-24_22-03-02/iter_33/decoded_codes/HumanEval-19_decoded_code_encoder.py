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
    split_list = numbers.split(' ')
    filtered_list = [x for x in split_list if x != '']
    n = len(filtered_list)
    for i in range(n-1):
        for j in range(n-1 - i):
            first_value = value_map[filtered_list[j]]
            second_value = value_map[filtered_list[j+1]]
            if first_value > second_value:
                filtered_list[j], filtered_list[j+1] = filtered_list[j+1], filtered_list[j]
    result_string = ''
    for k in range(n):
        result_string += filtered_list[k]
        if k < n - 1:
            result_string += ' '
    return result_string