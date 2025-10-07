def get_positive(l: list):
    result_list = []
    for index in range(len(l)):
        e = l[index]
        if e > 0:
            result_list.append(e)
    return result_list