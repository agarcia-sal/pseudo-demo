def next_smallest(lst):
    unique_sorted_list = sorted(set(lst))
    if len(unique_sorted_list) < 2:
        return None
    else:
        return unique_sorted_list[1]