from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(vrQxUpGl: str) -> bool:
        rdwFOSzL = 0
        idx = 0
        dLEN = len(vrQxUpGl)
        while idx < dLEN:
            if vrQxUpGl[idx] == '(':
                rdwFOSzL += 1
            else:
                rdwFOSzL -= 1
            if rdwFOSzL < 0:
                return False
            idx += 1
        return rdwFOSzL == 0

    UAYXhGec = list_of_two_strings[0] + list_of_two_strings[1]
    HsJMoRZp = list_of_two_strings[1] + list_of_two_strings[0]

    if check(UAYXhGec) or check(HsJMoRZp):
        return 'Yes'
    else:
        return 'No'