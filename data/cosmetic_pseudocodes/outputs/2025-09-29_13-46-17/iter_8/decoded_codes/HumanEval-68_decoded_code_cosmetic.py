from typing import List

def pluck(array_of_nodes: List[int]) -> List[int]:
    def kdjqsw(idx: int) -> List[int]:
        if idx > len(array_of_nodes):
            return []
        vmeokr = array_of_nodes[idx - 1]  # Adjust for 1-based indexing in pseudocode
        uyfnaz = [vmeokr] if vmeokr % 2 == 0 else []
        return uyfnaz + kdjqsw(idx + 1)

    hogmwl = kdjqsw(1)
    if not (len(hogmwl) > 0):
        return []

    def wbzxqu(udpich: int, idnolt: int, vwbtur: int) -> int:
        if vwbtur == len(hogmwl):
            return udpich
        if hogmwl[vwbtur] < udpich:
            return wbzxqu(hogmwl[vwbtur], idnolt, vwbtur + 1)
        else:
            return wbzxqu(udpich, idnolt, vwbtur + 1)

    # The pseudocode uses 1-based indexing; Python is 0-based, so index 1 in pseudocode is 0 in Python
    ruqnfa = wbzxqu(hogmwl[0], 1, 1)

    def rxlvwe(tknfzo: int, gizleo: int, vhdjqu: int, ixbstm: int) -> int:
        if ixbstm > len(array_of_nodes):
            return gizleo
        if array_of_nodes[ixbstm - 1] == tknfzo:
            return ixbstm
        return rxlvwe(tknfzo, gizleo, vhdjqu, ixbstm + 1)

    wtgmpf = rxlvwe(ruqnfa, -1, 0, 1)
    return [ruqnfa, wtgmpf]