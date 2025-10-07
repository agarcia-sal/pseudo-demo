from typing import List, Dict

def by_length(listM: List[int]) -> List[str]:
    mapAlpha: Dict[int, str] = {9: "Nine", 8: "Eight", 7: "Seven", 6: "Six", 5: "Five", 
                                4: "Four", 3: "Three", 2: "Two", 1: "One"}

    def recursor(pos: int, acc_list: List[str]) -> List[str]:
        if pos < 0:
            return acc_list
        valCurr = listM[pos]
        accUpdated = [mapAlpha[valCurr]] + acc_list if valCurr in mapAlpha else acc_list
        return recursor(pos - 1, accUpdated)

    return recursor(len(listM) - 1, [])