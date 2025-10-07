from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    return sorted(sorted(array_of_integers), key=lambda element: bin(element).count('1'))