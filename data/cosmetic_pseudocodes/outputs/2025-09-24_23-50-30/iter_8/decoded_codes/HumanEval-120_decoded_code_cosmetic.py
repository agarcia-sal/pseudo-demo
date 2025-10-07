from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    results: List[int] = []
    if positive_integer_k <= 0:
        return results
    temp_array: List[int] = []
    for each_element in array_of_integers:
        temp_array.append(each_element)
    n: int = len(temp_array)
    for i in range(1, n):
        for j in range(n - i):
            if temp_array[j] > temp_array[j + 1]:
                temp_array[j], temp_array[j + 1] = temp_array[j + 1], temp_array[j]
    results.extend(temp_array[n - positive_integer_k : n])
    return results