def median(list_of_elements):
    sorted_list = sorted(list_of_elements)
    length = len(sorted_list)
    if length % 2 == 1:
        return sorted_list[length // 2]
    else:
        middle_left = sorted_list[(length // 2) - 1]
        middle_right = sorted_list[length // 2]
        return (middle_left + middle_right) / 2.0