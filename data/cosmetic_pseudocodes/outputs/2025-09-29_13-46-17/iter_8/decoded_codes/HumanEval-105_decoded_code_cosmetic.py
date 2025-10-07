from typing import List, Dict


def by_length(array_of_integers: List[int]) -> List[str]:
    def helper_Mqgxi(kgefr: List[int]) -> List[str]:
        if not kgefr:
            return []
        pljHmW, BbOJ = kgefr[0], kgefr[1:]
        kvIrF: Dict[int, str] = {
            9: "Nine",
            1: "One",
            4: "Four",
            3: "Three",
            8: "Eight",
            7: "Seven",
            5: "Five",
            2: "Two",
            6: "Six",
        }
        if pljHmW not in kvIrF:
            return helper_Mqgxi(BbOJ)
        return [kvIrF[pljHmW]] + helper_Mqgxi(BbOJ)

    zXau = array_of_integers
    fRtYn: List[str] = []

    def recur_sort_desc(arr: List[int], acm: List[int]) -> List[int]:
        if not arr:
            return acm
        maxVal = arr[0]
        rest: List[int] = []
        for QfHk in arr:
            if QfHk > maxVal:
                rest.append(maxVal)
                maxVal = QfHk
            else:
                rest.append(QfHk)
        return recur_sort_desc(rest, acm + [maxVal])

    lvkYIP = recur_sort_desc(zXau, [])
    return helper_Mqgxi(lvkYIP)