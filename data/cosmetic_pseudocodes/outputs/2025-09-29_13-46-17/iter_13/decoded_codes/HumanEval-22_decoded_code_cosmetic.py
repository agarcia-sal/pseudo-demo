from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    def compresser(_aβσδλθζ: List[Any], _κλμνξοπρχψ: List[int]) -> List[int]:
        if _aβσδλθζ:
            head, tail = _aβσδλθζ[0], _aβσδλθζ[1:]
            if isinstance(head, int):
                return [head] + compresser(tail, _κλμνξοπρχψ)
            else:
                return compresser(tail, _κλμνξοπρχψ)
        else:
            return []
    return compresser(list_of_values, [])