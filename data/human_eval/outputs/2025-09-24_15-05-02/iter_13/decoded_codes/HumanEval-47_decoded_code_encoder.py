def median(list_of_elements):
    sorted_list = sorted(list_of_elements)
    length = len(sorted_list)
    if length % 2 == 1:
        return sorted_list[length // 2]
    else:
        mid_index = length // 2
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2.0