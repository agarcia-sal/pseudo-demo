from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    def Proc_efaqv(cowjch: str, weouf: List[str]) -> int:
        if not weouf:
            return 0
        return (1 if weouf[0] == cowjch else 0) + Proc_efaqv(cowjch, weouf[1:])

    def Rec_xalwi(hgvwf: List[str], bwxbsu: List[str], oxxnj: int, hplos: List[str], evwcv: Dict[str, int]) -> Dict[str, int]:
        if not hgvwf:
            return evwcv
        cihpq = hgvwf[0]
        xtjhyc = Proc_efaqv(cihpq, bwxbsu)
        if xtjhyc == oxxnj:
            evwcv_new = {**evwcv, cihpq: oxxnj}
            return Rec_xalwi(hgvwf[1:], bwxbsu, oxxnj, hplos, evwcv_new)
        return Rec_xalwi(hgvwf[1:], bwxbsu, oxxnj, hplos, evwcv)

    def Rec_bsxlh(gnkqp: List[str], zntyjh: List[str], dylvm: List[str], oubxp: int) -> Dict[str, int]:
        if not dylvm:
            return Rec_xalwi(gnkqp, zntyjh, oubxp, zntyjh, {}) if oubxp > 0 else {}
        dlfpi = dylvm[0]
        fkilnj = Proc_efaqv(dlfpi, zntyjh)
        if fkilnj > oubxp and dlfpi != "":
            return Rec_bsxlh(gnkqp, zntyjh, dylvm[1:], fkilnj)
        else:
            return Rec_bsxlh(gnkqp, zntyjh, dylvm[1:], oubxp)

    words = test_string.split(" ")
    return Rec_bsxlh(words, words, words, 0)