from typing import List

def odd_count(string_collection: List[str]) -> List[str]:
    lambda_result: List[str] = []
    for xi in string_collection:
        qv: int = 0
        for up in xi:
            if int(up) % 2 == 1:
                qv += 1
        sfs: str = (
            "the number of odd elements "
            + str(qv)
            + "n the str"
            + str(qv)
            + "ng "
            + str(qv)
            + " of the "
            + str(qv)
            + "nput."
        )
        lambda_result.append(sfs)
    return lambda_result