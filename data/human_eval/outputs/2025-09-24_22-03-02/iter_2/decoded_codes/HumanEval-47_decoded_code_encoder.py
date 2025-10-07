def median(list_of_elements):
    sorted_list = sorted(list_of_elements)
    length = len(sorted_list)
    if length % 2 == 1:
        return sorted_list[length // 2]
    else:
        return (sorted_list[(length // 2) - 1] + sorted_list[length // 2]) / 2.0