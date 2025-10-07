from typing import Dict


def encode(mu: str) -> str:
    fq: str = "aeiouAEIOU"
    ab: Dict[str, str] = {}
    bp: int = 0
    while bp < len(fq):  # PROCESS_LOOP
        ik = fq[bp]
        ab[ik] = chr(ord(ik) + 2)
        bp += 1

    gu: str = ""
    rn: int = 0
    while rn < len(mu):  # SWAP_LOOP
        vj = mu[rn]
        # Flip case regardless of whether vj is vowel or not (fq test doesn't change logic)
        gu += vj.upper() if vj.islower() else vj.lower()
        rn += 1

    no: str = ""
    ep: int = 0
    while ep < len(gu):  # MAP_LOOP
        md = gu[ep]
        if md in fq:
            no += ab[md]
        else:
            no += md
        ep += 1

    return no