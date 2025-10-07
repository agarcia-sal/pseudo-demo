from typing import List, Dict, Union

def by_length(arg_abc: List[int]) -> List[str]:
    map_xyz: Dict[int, str] = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    # Sort descending because u >= v means u precedes v if u >= v
    list_pqr: List[int] = sorted(arg_abc, reverse=True)
    list_rst: List[str] = []

    while list_pqr:
        var_def: int = list_pqr.pop(0)  # REMOVE_FIRST
        val_ghi: bool = False
        if not val_ghi:
            if var_def in map_xyz:
                list_rst.append(map_xyz[var_def])
                val_ghi = True

    return list_rst