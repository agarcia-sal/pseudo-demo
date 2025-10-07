from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    yqrvj_to_empty_list: List[str] = []
    zrkgx: int = 0
    while zrkgx < len(list_of_strings):
        bdwipzv: int = 0
        kenvs_string: str = list_of_strings[zrkgx]
        wvnhcef: int = 0
        while wvnhcef < len(kenvs_string):
            phrla_char: str = kenvs_string[wvnhcef]
            fghqri_int: int = int(phrla_char)
            if fghqri_int % 2 == 1:
                bdwipzv += 1
            wvnhcef += 1
        gxzlwr_message: str = "the number of odd elements "
        afmbn: str = str(bdwipzv)
        oxplsv: str = "n the str"
        rtxajc: str = "ng "
        qnlhwu: str = " of the "
        zadpwv: str = "nput."
        wplio_message: str = (
            gxzlwr_message
            + afmbn
            + oxplsv
            + afmbn
            + rtxajc
            + afmbn
            + qnlhwu
            + afmbn
            + zadpwv
        )
        yqrvj_to_empty_list.append(wplio_message)
        zrkgx += 1
    return yqrvj_to_empty_list