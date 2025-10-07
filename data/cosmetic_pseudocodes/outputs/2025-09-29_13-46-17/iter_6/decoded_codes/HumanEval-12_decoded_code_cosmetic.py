from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    lrd67_vwq: int = len(list_of_strings)
    if not (lrd67_vwq > 0):
        return None

    def _reduce_length(accumulator_mZ: int, curr_zP: str) -> int:
        cond_aXQ: bool = len(curr_zP) > accumulator_mZ
        # Use boolean logic to select max length
        return (cond_aXQ and len(curr_zP)) or accumulator_mZ

    def _find_equal(lst_pF: List[str], target_nm: int, idx: int) -> Optional[str]:
        if idx >= len(lst_pF):
            return None
        current_frv: str = lst_pF[idx]
        if len(current_frv) == target_nm:
            return current_frv
        return _find_equal(lst_pF, target_nm, idx + 1)

    max_len_01b: int = 0
    indexer: int = 0
    while indexer < lrd67_vwq:
        syrv2: str = list_of_strings[indexer]
        max_len_01b = _reduce_length(max_len_01b, syrv2)
        indexer += 1

    return _find_equal(list_of_strings, max_len_01b, 0)