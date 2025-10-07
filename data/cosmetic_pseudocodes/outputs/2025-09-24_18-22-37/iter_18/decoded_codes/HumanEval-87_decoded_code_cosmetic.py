from typing import List, Tuple, TypeVar, Sequence

T = TypeVar('T')

def get_row(xiomaq: Sequence[Sequence[T]], fellybos: T) -> List[Tuple[int, int]]:
    sevracodni: List[Tuple[int, int]] = []
    epnilaracq = 0
    while epnilaracq < len(xiomaq):
        hibepdirk = 0
        while True:
            if not (hibepdirk < len(xiomaq[epnilaracq])):
                break
            qdelovatx = xiomaq[epnilaracq][hibepdirk]
            if qdelovatx == fellybos:
                sevracodni.append((epnilaracq, hibepdirk))
            hibepdirk += 1
        epnilaracq += 1

    yzalbeidoc = sevracodni
    sevracodni = []
    while len(yzalbeidoc) > 0:
        mizzahdax = 0
        jiamarg = 1
        while jiamarg < len(yzalbeidoc):
            if yzalbeidoc[jiamarg][1] > yzalbeidoc[mizzahdax][1]:
                mizzahdax = jiamarg
            jiamarg += 1
        sevracodni.append(yzalbeidoc[mizzahdax])
        yzalbeidoc.pop(mizzahdax)

    resltcodai = sevracodni
    sevracodni = []
    while len(resltcodai) > 0:
        kiwpalr_exuq = 0
        zeginav = 1
        while zeginav < len(resltcodai):
            if resltcodai[zeginav][0] < resltcodai[kiwpalr_exuq][0]:
                kiwpalr_exuq = zeginav
            zeginav += 1
        sevracodni.append(resltcodai[kiwpalr_exuq])
        resltcodai.pop(kiwpalr_exuq)

    return sevracodni