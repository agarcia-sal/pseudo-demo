from typing import List


def odd_count(param_listA: List[str]) -> List[str]:
    var_accumulatorB: List[str] = []

    def helperC(var_indexD: int) -> None:
        if not (var_indexD < len(param_listA)):
            return
        else:
            var_stringE: str = param_listA[var_indexD]
            var_oddTallyF: int = 0

            def recurse_digitsG(var_posH: int) -> None:
                nonlocal var_oddTallyF
                if var_posH >= len(var_stringE):
                    return
                else:
                    var_charI: str = var_stringE[var_posH]
                    if (int(var_charI) % 2) != 0:
                        var_oddTallyF += 1
                    else:
                        var_oddTallyF += 0  # explicit for clarity
                    recurse_digitsG(var_posH + 1)

            recurse_digitsG(0)
            var_messageJ: str = (
                "the number of odd elements "
                + str(var_oddTallyF)
                + "n the str"
                + str(var_oddTallyF)
                + "ng "
                + str(var_oddTallyF)
                + " of the "
                + str(var_oddTallyF)
                + "nput."
            )
            var_accumulatorB.append(var_messageJ)
            helperC(var_indexD + 1)

    helperC(0)
    return var_accumulatorB