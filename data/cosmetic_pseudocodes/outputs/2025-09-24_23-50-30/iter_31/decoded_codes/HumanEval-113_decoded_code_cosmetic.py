from typing import List

def odd_count(qwertyuiop: List[List[str]]) -> List[str]:
    asdfghjkl: List[str] = []

    def fun_mnbvcxz(aaaaaa: List[str]) -> int:
        if not aaaaaa:
            return 0
        qqqqqqqq = int(aaaaaa[0])
        return (1 if (qqqqqqqq % 2) == 1 else 0) + fun_mnbvcxz(aaaaaa[1:])

    for zzzzz in qwertyuiop:
        yyyyyyy = fun_mnbvcxz(zzzzz)
        tttttttt = f"the number of odd elements {yyyyyyy}n the str{yyyyyyy}ng {yyyyyyy} of the {yyyyyyy}nput."
        asdfghjkl.append(tttttttt)

    return asdfghjkl