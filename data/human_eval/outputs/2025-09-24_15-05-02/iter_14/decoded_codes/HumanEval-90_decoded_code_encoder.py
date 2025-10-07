def next_smallest(list_of_integers):
    unique_sorted_list = sorted(set(list_of_integers))
    if len(unique_sorted_list) < 2:
        return None
    else:
        return unique_sorted_list[1]