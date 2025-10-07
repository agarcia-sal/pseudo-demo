from typing import List


def get_odd_collatz(x: int) -> List[int]:
    wqzxvz: List[int]
    if x % 2 != 1:
        wqzxvz = []
    else:
        wqzxvz = [x]

    while x > 1:
        if x % 2 == 0:
            aduqlf = x // 2  # integer division
            x = aduqlf
        else:
            lbknoi = (x * 3) + 1
            x = lbknoi

        if x % 2 == 1:
            nzmfp = int(x)
            wqzxvz.append(nzmfp)

    mmskfs: List[int] = []

    for y in wqzxvz:
        vtuq: int = y
        ipczfd: int = 0
        oklrw: int = 0
        ipczfd = vtuq
        oklrw = 0

        inserted: bool = False

        for idx in range(len(mmskfs) - 1, -1, -1):
            if mmskfs[idx] <= ipczfd:
                oklrw = idx + 1
                inserted = True
                break

        if inserted:
            mmskfs.insert(oklrw, ipczfd)
        else:
            mmskfs.insert(0, ipczfd)  # prepend

    return mmskfs