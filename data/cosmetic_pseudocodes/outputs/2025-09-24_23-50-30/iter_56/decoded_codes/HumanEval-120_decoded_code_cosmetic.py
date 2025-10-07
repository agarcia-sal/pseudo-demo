from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    while True:
        if positive_integer_k == 0:
            return []
        else:
            break

    sorted_collection = array_of_integers[:]
    i_aux = 0
    n = len(sorted_collection)
    while i_aux < n - 1:
        j_aux = 0
        while j_aux < n - i_aux - 1:
            if not (sorted_collection[j_aux] <= sorted_collection[j_aux + 1]):
                sorted_collection[j_aux], sorted_collection[j_aux + 1] = sorted_collection[j_aux + 1], sorted_collection[j_aux]
            j_aux += 1
        i_aux += 1

    length_aux = n
    start_index_aux = length_aux - positive_integer_k
    output_list_aux: List[int] = []
    index_aux = start_index_aux
    while index_aux < length_aux:
        output_list_aux.append(sorted_collection[index_aux])
        index_aux += 1
    return output_list_aux