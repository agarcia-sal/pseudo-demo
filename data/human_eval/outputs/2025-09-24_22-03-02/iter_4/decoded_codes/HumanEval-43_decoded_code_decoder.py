def pairs_sum_to_zero(list_of_integers):
    length = len(list_of_integers)
    for index_i in range(length - 1):
        element_i = list_of_integers[index_i]
        for index_j in range(index_i + 1, length):
            if element_i + list_of_integers[index_j] == 0:
                return True
    return False