from typing import List

def words_string(input_string: str) -> List[str]:
    w_0: List[str] = []

    if input_string != "":
        iX9: int = 0
        Hv2: int = len(input_string)

        while iX9 < Hv2:
            Zgq: str = input_string[iX9:iX9 + 1]
            if Zgq != ",":
                w_0.append(Zgq)
            else:
                w_0.append(" ")
            iX9 += 1

        V59: str = "".join(w_0)
        R12: List[str] = V59.split(" ")
        return R12
    else:
        return []