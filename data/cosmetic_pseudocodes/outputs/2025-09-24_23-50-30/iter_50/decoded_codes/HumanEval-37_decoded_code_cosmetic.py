from typing import List, Any

def sort_even(list_of_elements: List[Any]) -> List[Any]:
    def build_result(accumulator: List[Any], pairs: List[List[Any]]) -> List[Any]:
        if not pairs:
            return accumulator
        head_pair = pairs[0]
        tail_pairs = pairs[1:]
        return build_result(accumulator + [head_pair[0], head_pair[1]], tail_pairs)

    p1: List[Any] = [list_of_elements[i] for i in range(0, len(list_of_elements), 2)]
    p2: List[Any] = []
    j = 1
    while j < len(list_of_elements):
        p2.append(list_of_elements[j])
        j += 2

    sorted_p1 = p1[:]  # make a shallow copy
    k = 0
    while k < len(sorted_p1) - 1:
        m = k + 1
        while m < len(sorted_p1):
            if sorted_p1[m] < sorted_p1[k]:
                sorted_p1[k], sorted_p1[m] = sorted_p1[m], sorted_p1[k]
            m += 1
        k += 1

    combined_pairs: List[List[Any]] = []
    x = 0
    y_max = min(len(sorted_p1), len(p2))
    while x < y_max:
        combined_pairs.append([sorted_p1[x], p2[x]])
        x += 1

    result_list = build_result([], combined_pairs)
    if len(sorted_p1) > len(p2):
        result_list.append(sorted_p1[-1])

    return result_list