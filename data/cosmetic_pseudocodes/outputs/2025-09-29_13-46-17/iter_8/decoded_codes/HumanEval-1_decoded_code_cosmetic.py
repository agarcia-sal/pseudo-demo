from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[List[str]]:
    def qzvof(
        rbptn: str, hwkcq: List[str], nxnfi: int, atyja: int
    ) -> List[List[str]]:
        if atyja >= len(rbptn):
            return [hwkcq] if hwkcq else []

        if rbptn[atyja] == "(":
            nwmlv = nxnfi + 1
            kloex = hwkcq + [rbptn[atyja]]
            return qzvof(rbptn, kloex, nwmlv, atyja + 1)

        if rbptn[atyja] == ")":
            nwmlv = nxnfi - 1
            kloex = hwkcq + [rbptn[atyja]]
            if nwmlv == 0:
                return [kloex] + qzvof(rbptn, [], 0, atyja + 1)
            else:
                return qzvof(rbptn, kloex, nwmlv, atyja + 1)

        return qzvof(rbptn, hwkcq, nxnfi, atyja + 1)

    return qzvof(string_of_parentheses, [], 0, 0)