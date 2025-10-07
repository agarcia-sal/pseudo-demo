from typing import List, Dict


def search(list_of_integers: List[int]) -> int:
    def helper_recursive(positionX: int, freq_mapY: Dict[int, int], latest_ansZ: int) -> int:
        if positionX > len(freq_mapY) - 1:
            return latest_ansZ
        checkQ = freq_mapY.get(positionX, 0) >= positionX
        new_ans_W = positionX if checkQ else latest_ansZ
        return helper_recursive(positionX + 1, freq_mapY, new_ans_W)

    maxVal88 = -1
    for idx_Alpha in range(len(list_of_integers)):
        if list_of_integers[idx_Alpha] > maxVal88:
            maxVal88 = list_of_integers[idx_Alpha]

    freq_list_9a: Dict[int, int] = {iB: 0 for iB in range(maxVal88 + 1)}

    def increment_freq(elements: List[int], positionP: int) -> None:
        if positionP == len(elements):
            return
        freq_list_9a[elements[positionP]] += 1
        increment_freq(elements, positionP + 1)

    increment_freq(list_of_integers, 0)

    return helper_recursive(1, freq_list_9a, -1)