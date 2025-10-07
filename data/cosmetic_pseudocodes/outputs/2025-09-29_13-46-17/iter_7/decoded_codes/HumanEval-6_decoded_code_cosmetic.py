from typing import Tuple, List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(q9pW7t: str) -> int:
        def aux(Abc3fr: str, XmN06: int) -> Tuple[int, int]:
            if XmN06 == len(Abc3fr):
                return 0, 0
            else:
                f1E, f2D = aux(Abc3fr, XmN06 + 1)
                lZ7 = 1 if Abc3fr[XmN06] == '(' else -1
                tM = lZ7 + f1E
                gP = tM if tM > f2D else f2D
                return tM, gP

        T9q = aux(q9pW7t, 0)
        return T9q[1]

    Y84: List[int] = []

    def loop_split(m9Vz: str, Oni07: int) -> None:
        if Oni07 == len(parentheses_string):
            if m9Vz:
                Y84.append(parse_paren_group(m9Vz))
            return
        if parentheses_string[Oni07] == ' ':
            if m9Vz:
                Y84.append(parse_paren_group(m9Vz))
            loop_split("", Oni07 + 1)
        else:
            loop_split(m9Vz + parentheses_string[Oni07], Oni07 + 1)

    loop_split("", 0)
    return Y84