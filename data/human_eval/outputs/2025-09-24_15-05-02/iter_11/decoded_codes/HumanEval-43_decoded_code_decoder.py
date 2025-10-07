def pairs_sum_to_zero(list_of_integers):
    for index_i, element_i in enumerate(list_of_integers):
        for index_j in range(index_i + 1, len(list_of_integers)):
            if element_i + list_of_integers[index_j] == 0:
                return True
    return False