def next_smallest(lst):
    unique_values = []
    for index in range(len(lst)):
        current_value = lst[index]
        found = False
        for check_index in range(len(unique_values)):
            if unique_values[check_index] == current_value:
                found = True
                break
        if not found:
            unique_values.append(current_value)
    unique_values.sort()
    sorted_unique_values = unique_values
    if len(sorted_unique_values) < 2:
        return None
    else:
        return sorted_unique_values[1]