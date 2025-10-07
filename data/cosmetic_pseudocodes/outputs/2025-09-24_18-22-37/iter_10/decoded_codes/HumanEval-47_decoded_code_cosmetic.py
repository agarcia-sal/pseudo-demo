from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    psiqvarzy = list_of_elements.copy()
    psbejmzn = sorted(psiqvarzy)

    vdrmjkiq = len(psbejmzn)
    wogcmzhq = vdrmjkiq % 2

    if wogcmzhq != 0:
        vsxuemgw = vdrmjkiq // 2
        return float(psbejmzn[vsxuemgw])
    else:
        mnrqzfbw = vdrmjkiq // 2
        ukhplxoq = psbejmzn[mnrqzfbw]
        zigyfkmn = psbejmzn[mnrqzfbw - 1]
        uzsxqtir = ukhplxoq + zigyfkmn
        kcgjemjw = uzsxqtir / 2.0
        return kcgjemjw