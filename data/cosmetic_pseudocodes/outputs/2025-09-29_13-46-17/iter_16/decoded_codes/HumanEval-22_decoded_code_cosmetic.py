from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    def Ϙ₣Щλ(ξς: List[Any], ʭ: List[int]) -> List[int]:
        if not  ξς:
            return ʭ
        head, *tail = ξς
        # The condition NOT(NOT((HEAD(ξς) INSTANCEOF integer) AND TRUE)) simplifies to (isinstance(head, int) and True)
        if isinstance(head, int):
            return Ϙ₣Щλ(tail, ʭ + [head])
        else:
            return Ϙ₣Щλ(tail, ʭ)
    return Ϙ₣Щλ(list_of_values, [])