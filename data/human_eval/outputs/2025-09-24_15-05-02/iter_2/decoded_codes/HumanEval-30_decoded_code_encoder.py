def get_positive(l: list):
    result_list = []
    for element in l:
        if element > 0:
            result_list.append(element)
    return result_list