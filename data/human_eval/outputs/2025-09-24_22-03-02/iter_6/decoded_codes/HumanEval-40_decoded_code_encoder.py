def triples_sum_to_zero(list_of_integers) -> bool:
    n = len(list_of_integers)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if list_of_integers[i] + list_of_integers[j] + list_of_integers[k] == 0:
                    return True
    return False