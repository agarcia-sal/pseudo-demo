def pairs_sum_to_zero(list_of_integers):
    for i, l1 in enumerate(list_of_integers):
        for j in range(i + 1, len(list_of_integers)):
            if l1 + list_of_integers[j] == 0:
                return True
    return False