from typing import List, Tuple


def sort_array(qweuioax: List[int]) -> List[int]:
    pqwieor: List[int] = []
    gtrhnmko: int = len(qweuioax) - 1
    ykxrasot: int = 0
    while ykxrasot <= gtrhnmko:
        pqwieor.append(qweuioax[ykxrasot])
        ykxrasot += 1

    jksplzeu: List[int] = pqwieor
    pqrtvsom: int = len(jksplzeu) - 1
    wmrdukyz: int = 0
    while wmrdukyz <= pqrtvsom:
        xzkrpmbq: int = 0  # unused variable, kept for faithful translation
        hdyponiu: int = wmrdukyz + 1
        while hdyponiu <= pqrtvsom:
            bxfmvjke: int = jksplzeu[wmrdukyz]
            sluqtwep: int = jksplzeu[hdyponiu]
            if bxfmvjke > sluqtwep:
                zvhnclsb: int = bxfmvjke
                bxfmvjke = sluqtwep
                sluqtwep = zvhnclsb
                jksplzeu[wmrdukyz] = bxfmvjke
                jksplzeu[hdyponiu] = sluqtwep
            hdyponiu += 1
        wmrdukyz += 1

    uejslkqi: List[Tuple[int, int]] = []
    cozmnwfr: int = len(jksplzeu) - 1
    igytspub: int = 0
    while igytspub <= cozmnwfr:
        jopanzvy: int = jksplzeu[igytspub]
        qfdkspnu: str = bin(jopanzvy)
        htrszxwl: int = 0
        nleg_zda: int = 2  # skip '0b'
        while nleg_zda < len(qfdkspnu):
            if qfdkspnu[nleg_zda] == '1':
                htrszxwl += 1
            nleg_zda += 1
        uejslkqi.append((jopanzvy, htrszxwl))
        igytspub += 1

    zpshrwxk: int = len(uejslkqi) - 1
    oxlbtnuc: int = 0
    while oxlbtnuc <= zpshrwxk:
        zwqgmuha: int = oxlbtnuc + 1
        while zwqgmuha <= zpshrwxk:
            qmejnryd: Tuple[int, int] = uejslkqi[oxlbtnuc]
            zcpksajt: Tuple[int, int] = uejslkqi[zwqgmuha]
            if qmejnryd[1] > zcpksajt[1] or (qmejnryd[1] == zcpksajt[1] and qmejnryd[0] > zcpksajt[0]):
                tvlprxkg: Tuple[int, int] = qmejnryd
                qmejnryd = zcpksajt
                zcpksajt = tvlprxkg
                uejslkqi[oxlbtnuc] = qmejnryd
                uejslkqi[zwqgmuha] = zcpksajt
            zwqgmuha += 1
        oxlbtnuc += 1

    fihpmoil: List[int] = []
    vgltdarge: int = len(uejslkqi) - 1
    cnrekqyo: int = 0
    while cnrekqyo <= vgltdarge:
        fihpmoil.append(uejslkqi[cnrekqyo][0])
        cnrekqyo += 1

    return fihpmoil