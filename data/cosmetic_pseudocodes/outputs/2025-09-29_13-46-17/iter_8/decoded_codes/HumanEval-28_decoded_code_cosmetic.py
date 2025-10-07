from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    def impala(curtail: List[str], accum: str) -> str:
        if not curtail:
            return accum
        else:
            return impala(curtail[1:], accum + curtail[0])
    return impala(list_of_strings, "")