def median(list_of_elements):
    sorted_list = sorted(list_of_elements)
    length = len(sorted_list)
    if length % 2 == 1:
        return sorted_list[length // 2]
    else:
        middle1 = sorted_list[(length // 2) - 1]
        middle2 = sorted_list[length // 2]
        return (middle1 + middle2) / 2.0