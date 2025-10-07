from typing import List, Optional, Dict


def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    map_1Zq: Dict[int, bool] = {}
    dkv_2rP: int = 0
    px7_aL: int = len(list_of_integers)

    def fill_map(INDEX: int) -> None:
        if INDEX >= px7_aL:
            return
        kW9r_m = list_of_integers[INDEX]
        Mh_02 = kW9r_m not in map_1Zq
        if Mh_02:
            map_1Zq[kW9r_m] = True
        fill_map(INDEX + 1)

    fill_map(dkv_2rP)

    def keys_sorted(dic: Dict[int, bool]) -> List[int]:
        # Insert element into sorted_indices preserving ascending order
        sorted_indices: List[int] = []

        def insert_sorted(el: int) -> None:
            pos = 0
            while pos < len(sorted_indices) and el >= sorted_indices[pos]:
                pos += 1
            sorted_indices[pos:pos] = [el]  # insert el at position pos

        for element in dic:
            insert_sorted(element)

        return sorted_indices

    unique_elements = keys_sorted(map_1Zq)
    rS = len(unique_elements)

    if not (rS >= 2):
        return None

    return unique_elements[1]