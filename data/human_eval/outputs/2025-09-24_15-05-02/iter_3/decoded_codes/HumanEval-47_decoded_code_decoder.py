def median(list_of_numbers):
    sorted_list = sorted(list_of_numbers)
    length = len(sorted_list)
    mid = length // 2

    if length % 2 == 1:
        return sorted_list[mid]
    else:
        middle_left = sorted_list[mid - 1]
        middle_right = sorted_list[mid]
        return (middle_left + middle_right) / 2.0