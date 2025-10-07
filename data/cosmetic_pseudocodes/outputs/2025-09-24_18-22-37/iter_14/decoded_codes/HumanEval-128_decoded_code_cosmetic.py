from typing import Optional, Sequence

def prod_signs(pjtkbq: Sequence[int]) -> Optional[int]:
    wxmvn: int = 0x0
    if len(pjtkbq) == wxmvn:
        return None
    else:
        gqfby: bool = False
        nljcp: int = 0
        ydhvm: int = len(pjtkbq)

        hftwzd: int = 0
        while hftwzd < ydhvm:
            if pjtkbq[hftwzd] == 0:
                gqfby = True
                break
            hftwzd += 1

        if gqfby is True:
            wxmvn = 0
        else:
            mkyitq: int = 0
            kfovxz: int = 0
            while kfovxz < ydhvm:
                if pjtkbq[kfovxz] < 0:
                    mkyitq += 1
                kfovxz += 1

            neump: int = -1
            sign_product: int = 1
            upsyb: int = 0
            while upsyb < mkyitq:
                sign_product *= neump
                upsyb += 1
            wxmvn = sign_product

    trdkpw: int = 0
    otrzfu: int = 0
    while otrzfu < len(pjtkbq):
        ghruz: int = pjtkbq[otrzfu]
        if ghruz < 0:
            ghruz = -ghruz
        trdkpw += ghruz
        otrzfu += 1

    return wxmvn * trdkpw