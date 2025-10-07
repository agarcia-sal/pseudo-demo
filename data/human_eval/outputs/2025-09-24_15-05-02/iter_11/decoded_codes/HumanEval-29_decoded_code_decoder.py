def filter_by_prefix(list_of_strings, prefix):
    filtered_list = []
    for string in list_of_strings:
        if string.startswith(prefix):
            filtered_list.append(string)
    return filtered_list