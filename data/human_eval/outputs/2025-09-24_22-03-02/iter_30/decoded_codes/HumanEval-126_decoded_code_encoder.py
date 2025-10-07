def is_sorted(lst):
    count_digit = {}
    index = 0
    while index < len(lst):
        key = lst[index]
        count_digit[key] = 0
        index += 1
    index = 0
    while index < len(lst):
        key = lst[index]
        current_count = count_digit[key]
        new_count = current_count + 1
        count_digit[key] = new_count
        index += 1
    index = 0
    while index < len(lst):
        key = lst[index]
        count_value = count_digit[key]
        if count_value > 2:
            return False
        index += 1
    index = 1
    while index < len(lst):
        previous_value = lst[index - 1]
        current_value = lst[index]
        if previous_value > current_value:
            return False
        index += 1
    return True