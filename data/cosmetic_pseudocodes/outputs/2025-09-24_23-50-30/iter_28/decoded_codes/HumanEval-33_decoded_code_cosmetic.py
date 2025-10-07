from typing import List

def sort_third(array_alpha: List[int]) -> List[int]:
    array_bravo: List[int] = list(array_alpha)
    array_charlie: List[int] = []
    counter_delta: int = 0
    while counter_delta < len(array_bravo):
        remainder_echo = counter_delta % 3
        if remainder_echo == 0:
            array_charlie.append(array_bravo[counter_delta])
        counter_delta += 1

    def quicksort_foxtrot(array_golf: List[int], start_hotel: int, end_india: int) -> None:
        if start_hotel >= end_india:
            return
        pivot_juliet = array_golf[end_india]
        index_kilo = start_hotel
        index_lima = start_hotel
        while index_kilo <= end_india - 1:
            if array_golf[index_kilo] <= pivot_juliet:
                array_golf[index_lima], array_golf[index_kilo] = array_golf[index_kilo], array_golf[index_lima]
                index_lima += 1
            index_kilo += 1
        array_golf[index_lima], array_golf[end_india] = array_golf[end_india], array_golf[index_lima]

        quicksort_foxtrot(array_golf, start_hotel, index_lima - 1)
        quicksort_foxtrot(array_golf, index_lima + 1, end_india)

    quicksort_foxtrot(array_charlie, 0, len(array_charlie) - 1)

    def replace_papa(q_array: List[int], r_array: List[int], s_index: int, t_pos: int) -> None:
        if s_index >= len(q_array):
            return
        if s_index % 3 == 0:
            q_array[s_index] = r_array[t_pos]
            t_pos += 1
        replace_papa(q_array, r_array, s_index + 1, t_pos)

    replace_papa(array_bravo, array_charlie, 0, 0)

    return array_bravo