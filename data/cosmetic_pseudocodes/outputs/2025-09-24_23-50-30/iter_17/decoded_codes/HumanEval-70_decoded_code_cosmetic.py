from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    accumulated: List[int] = []
    toggle: int = 1
    while list_of_integers:
        if toggle == 1:
            candidate = list_of_integers[0]
            for index in range(1, len(list_of_integers)):
                if list_of_integers[index] < candidate:
                    candidate = list_of_integers[index]
            accumulated.append(candidate)
            for index in range(len(list_of_integers)):
                if list_of_integers[index] == candidate:
                    del list_of_integers[index]
                    break
        else:
            candidate = list_of_integers[0]
            pos = 0
            for index in range(len(list_of_integers)):
                if list_of_integers[index] > candidate:
                    candidate = list_of_integers[index]
                    pos = index
            accumulated.append(candidate)
            del list_of_integers[pos]
        toggle = 1 - toggle
    return accumulated