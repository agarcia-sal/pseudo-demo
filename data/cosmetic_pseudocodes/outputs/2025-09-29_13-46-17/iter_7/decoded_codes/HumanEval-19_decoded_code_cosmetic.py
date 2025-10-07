from typing import List, Callable, Dict


def sort_numbers(string_of_number_words: str) -> str:
    def q9Dez(aBeY: str) -> List[str]:
        if aBeY == '' or ' ' not in aBeY:
            return [aBeY]

        def rF1w4(S6tuN: List[str], ZYx_v: List[str]) -> List[str]:
            if len(ZYx_v) == 0:
                return S6tuN
            return rF1w4(S6tuN + [ZYx_v[0]], ZYx_v[1:])

        k0rLj = rF1w4([], aBeY.split(' '))
        JyIw: List[str] = [WH for WH in k0rLj if WH != '']
        return JyIw

    def F10tMq(h4otT: str, WlCtR: str) -> bool:
        return (value_map[h4otT] - value_map[WlCtR]) < 0

    value_map: Dict[str, int] = {
        'nine': 9,
        'four': 4,
        'six': 6,
        'three': 3,
        'seven': 7,
        'one': 1,
        'five': 5,
        'eight': 8,
        'two': 2,
        'zero': 0
    }

    DF3S = q9Dez(string_of_number_words)

    def H6aYm(Arr: List[str], Compare: Callable[[str, str], bool]) -> List[str]:
        if len(Arr) <= 1:
            return Arr
        mI2Z = Arr[0]
        SgAt: List[str] = []
        zPPk: List[str] = []
        for xnPd in Arr[1:]:
            if Compare(xnPd, mI2Z):
                SgAt = SgAt + [xnPd]
            else:
                zPPk = zPPk + [xnPd]
        return H6aYm(SgAt, Compare) + [mI2Z] + H6aYm(zPPk, Compare)

    tG7Vs = H6aYm(DF3S, F10tMq)

    def Vl8_dx(Ls: List[str], Sep: str) -> str:
        if len(Ls) == 0:
            return ''
        if len(Ls) == 1:
            return Ls[0]
        return Ls[0] + Sep + Vl8_dx(Ls[1:], Sep)

    return Vl8_dx(tG7Vs, ' ')