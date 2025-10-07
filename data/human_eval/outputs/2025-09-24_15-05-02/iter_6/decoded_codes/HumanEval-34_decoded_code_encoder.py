def unique(list_of_elements):
    unique_elements_set = set(list_of_elements)
    unique_elements_list = list(unique_elements_set)
    unique_elements_list.sort()
    return unique_elements_list