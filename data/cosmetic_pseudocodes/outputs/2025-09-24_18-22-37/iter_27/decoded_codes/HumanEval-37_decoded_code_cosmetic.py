from typing import List, TypeVar

T = TypeVar('T')

def sort_even(qryzrz: List[T]) -> List[T]:
    ftqtek: List[T] = []
    cfdafm: List[T] = []
    qklruw: int = 0

    while qklruw < len(qryzrz):
        if (qklruw % 2) == 0:
            ftqtek.append(qryzrz[qklruw])
        else:
            cfdafm.append(qryzrz[qklruw])
        qklruw += 1

    nqcneo: int = len(ftqtek)
    jbwfwc: int = 0

    # Selection sort on ftqtek
    while jbwfwc < nqcneo - 1:
        hwnbsm = jbwfwc
        kdkifx = jbwfwc + 1
        while kdkifx < nqcneo:
            if ftqtek[kdkifx] < ftqtek[hwnbsm]:
                hwnbsm = kdkifx
            kdkifx += 1
        if hwnbsm != jbwfwc:
            ftqtek[jbwfwc], ftqtek[hwnbsm] = ftqtek[hwnbsm], ftqtek[jbwfwc]
        jbwfwc += 1

    ztfkyr: List[T] = []
    dgtyoz: int = 0
    gvhash: int = 0

    while dgtyoz < len(ftqtek) and gvhash < len(cfdafm):
        ztfkyr.append(ftqtek[dgtyoz])
        ztfkyr.append(cfdafm[gvhash])
        dgtyoz += 1
        gvhash += 1

    if len(ftqtek) > len(cfdafm):
        ztfkyr.append(ftqtek[-1])

    return ztfkyr