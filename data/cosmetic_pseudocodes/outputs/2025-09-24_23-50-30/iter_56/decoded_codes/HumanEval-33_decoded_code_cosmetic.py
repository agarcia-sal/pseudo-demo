from typing import List

def sort_third(array_alpha: List[int]) -> List[int]:
    array_bravo: List[int] = []
    array_charlie: List[int] = []
    index_delta: int = 0
    length_echo: int = len(array_alpha)
    while index_delta < length_echo:
        remainder_foxtrot: int = index_delta - (3 * (index_delta // 3))
        if remainder_foxtrot == 0:
            array_bravo.append(array_alpha[index_delta])
        index_delta += 1
    array_charlie = sorted(array_bravo)

    def procedure_uniform(array_golf: List[int], array_hotel: List[int], array_india: int, value_juliet: int) -> List[int]:
        if array_india == len(array_golf):
            return array_golf
        kappa: int = array_india * 3
        array_golf[kappa] = array_hotel[value_juliet]
        return procedure_uniform(array_golf, array_hotel, array_india + 1, value_juliet + 1)

    array_kilo: List[int] = procedure_uniform(array_alpha, array_charlie, 0, 0)
    return array_kilo