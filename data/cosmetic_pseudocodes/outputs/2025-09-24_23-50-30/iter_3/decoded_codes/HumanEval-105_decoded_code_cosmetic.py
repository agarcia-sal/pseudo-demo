from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    num_words: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    reversed_array = array_of_integers[:]
    n = len(reversed_array)
    # Sort reversed_array in descending order using a selection sort method
    for i in range(n - 1):
        for j in range(i + 1, n):
            if reversed_array[j] > reversed_array[i]:
                reversed_array[i], reversed_array[j] = reversed_array[j], reversed_array[i]
    output: List[str] = []
    idx = 0
    while idx < n:
        if reversed_array[idx] in num_words:
            output.append(num_words[reversed_array[idx]])
        idx += 1
    return output