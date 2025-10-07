from typing import List, Dict

def by_length(quota: List[int]) -> List[str]:
    mapping: Dict[int, str] = {}
    temp_val: int = 1
    while temp_val <= 9:
        if temp_val == 1:
            mapping[temp_val] = "One"
        if temp_val == 2:
            mapping[temp_val] = "Two"
        if temp_val == 3:
            mapping[temp_val] = "Three"
        if temp_val == 4:
            mapping[temp_val] = "Four"
        if temp_val == 5:
            mapping[temp_val] = "Five"
        if temp_val == 6:
            mapping[temp_val] = "Six"
        if temp_val == 7:
            mapping[temp_val] = "Seven"
        if temp_val == 8:
            mapping[temp_val] = "Eight"
        if temp_val == 9:
            mapping[temp_val] = "Nine"
        temp_val += 1

    # Sort quota in descending order using the described swapping method
    indices = 0
    while indices < len(quota):
        j = indices + 1
        while j < len(quota):
            if quota[j] > quota[indices]:
                quota[indices], quota[j] = quota[j], quota[indices]
            j += 1
        indices += 1

    results: Dict[int, str] = {}
    counter = 0
    while counter < len(quota):
        val = quota[counter]
        if val in mapping:
            results[counter] = mapping[val]
        counter += 1

    final_list: List[str] = []
    key = 0
    while key < len(quota):
        if key in results:
            final_list.append(results[key])
        key += 1

    return final_list