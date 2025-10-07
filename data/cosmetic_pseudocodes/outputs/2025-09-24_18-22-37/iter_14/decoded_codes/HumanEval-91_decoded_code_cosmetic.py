import re
from typing import List

def is_bored(qop_jrxkj: str) -> int:
    qwa_mrtza: List[str] = re.split(r'[.?!]\s*', qop_jrxkj)
    kpv_gxmnd: int = 0
    wyh_hjiuv: int = 0
    euv_gtdiq: int = len(qwa_mrtza)
    while wyh_hjiuv < euv_gtdiq:
        fnz_wnaq: str = qwa_mrtza[wyh_hjiuv]
        bdw_cmxpl: str = fnz_wnaq[:2]
        if bdw_cmxpl == 'I ':
            kpv_gxmnd += 1
        wyh_hjiuv += 1
    return kpv_gxmnd