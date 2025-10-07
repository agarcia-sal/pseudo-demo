from typing import List

def find_max(list_of_words: List[str]) -> str:
    def comparator(a: str, b: str) -> int:
        set_a = set(a)
        set_b = set(b)
        len_a = len(set_a)
        len_b = len(set_b)
        if len_a > len_b:
            return -1
        elif len_a < len_b:
            return 1
        else:
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0

    sorted_array = [word for word in list_of_words]
    n = len(sorted_array)

    while True:
        changed = False
        for i in range(n - 1):
            if comparator(sorted_array[i], sorted_array[i + 1]) > 0:
                sorted_array[i], sorted_array[i + 1] = sorted_array[i + 1], sorted_array[i]
                changed = True
        n -= 1
        if not changed:
            break

    return sorted_array[0]