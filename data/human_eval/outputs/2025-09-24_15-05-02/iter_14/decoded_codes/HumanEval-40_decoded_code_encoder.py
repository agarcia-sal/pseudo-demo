def triples_sum_to_zero(list_l):
    for i in range(len(list_l) - 1):
        for j in range(i + 1, len(list_l) - 1):
            for k in range(j + 1, len(list_l) - 1):
                if list_l[i] + list_l[j] + list_l[k] == 0:
                    return True
    return False