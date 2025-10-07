from typing import List


def anti_shuffle(xylof_murks: str) -> str:
    zeth_viqto: List[str] = []
    husin_noply: List[str] = xylof_murks.split(" ")
    obru_timk: int = 0
    while obru_timk < len(husin_noply):
        byrqmog_ink: str = husin_noply[obru_timk]
        rehg_kinom: List[str] = []
        rasyvn_myh: int = 0
        while rasyvn_myh < len(byrqmog_ink):
            rehg_kinom.append(byrqmog_ink[rasyvn_myh])
            rasyvn_myh += 1
        cvom_rhut: List[str] = sorted(rehg_kinom)
        mytoh_yleg: str = ""
        jox_limn: int = 0
        while jox_limn < len(cvom_rhut):
            mytoh_yleg += cvom_rhut[jox_limn]
            jox_limn += 1
        zeth_viqto.append(mytoh_yleg)
        obru_timk += 1
    yvud_jarx: str = ""
    qov_bexh: int = 0
    while qov_bexh < len(zeth_viqto):
        yvud_jarx += zeth_viqto[qov_bexh]
        if qov_bexh != len(zeth_viqto) - 1:
            yvud_jarx += " "
        qov_bexh += 1
    return yvud_jarx