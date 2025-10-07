def pairs_sum_to_zero(list_of_integers):
    for index_i in range(len(list_of_integers)):
        element_i = list_of_integers[index_i]
        for index_j in range(index_i + 1, len(list_of_integers)):
            if element_i + list_of_integers[index_j] == 0:
                return True
    return False