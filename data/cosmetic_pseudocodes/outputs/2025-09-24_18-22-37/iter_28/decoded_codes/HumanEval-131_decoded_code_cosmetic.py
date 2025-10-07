from typing import Union

def digits(qw: Union[int, str]) -> int:
    km: int = 1
    rv: int = 0
    xi: int = 0
    qw_str: str = str(qw)

    while xi < len(qw_str):
        bq: int = int(qw_str[xi])
        jt: int = bq % 2
        if jt == 1:
            km *= bq
            rv += 1
        # no else needed for default case (no operation)
        xi += 1

    tw: bool = (rv == 0)
    if tw:
        return 0
    return km