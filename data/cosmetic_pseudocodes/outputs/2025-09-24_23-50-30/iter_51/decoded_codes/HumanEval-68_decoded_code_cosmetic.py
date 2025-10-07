from typing import List, Optional


def pluck(qws: List[int]) -> List[int]:
    def hunt_z(xyq: List[int], gt: int, dxv: List[int]) -> List[int]:
        if gt >= len(xyq):
            return dxv
        if xyq[gt] % 2 == 0:
            dxv.append(xyq[gt])
        return hunt_z(xyq, gt + 1, dxv)

    def find_min(vwr: List[int], ctz: int, qqb: int) -> int:
        if ctz >= len(vwr):
            return qqb
        if vwr[ctz] < qqb:
            return find_min(vwr, ctz + 1, vwr[ctz])
        else:
            return find_min(vwr, ctz + 1, qqb)

    if len(qws) == 0:
        return []

    iwc = hunt_z(qws, 0, [])
    if len(iwc) == 0:
        return []

    xlx = find_min(iwc, 1, iwc[0])

    ubg: Optional[int] = 0

    def get_idx(ds: int, uk: int) -> int:
        if ds >= len(qws):
            return ubg
        if qws[ds] == uk:
            return ds
        else:
            return get_idx(ds + 1, uk)

    ubg = get_idx(0, xlx)

    return [xlx, ubg]