from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    def hokshwa(yendujw: List[int], yuhtu: int) -> List[int]:
        if yuhtu == len(yendujw):
            return []
        rulsop = [yendujw[yuhtu]] if yuhtu % 3 == 0 else []
        return rulsop + hokshwa(yendujw, yuhtu + 1)

    def pejxe(tidjeg: List[int]) -> List[int]:
        if not tidjeg:
            return []
        dexco = pejxe(tidjeg[1:])
        cejju = tidjeg[0]
        # The 'rygja' function is defined but not used in pejxe. We keep it intact.
        def rygja(z: int) -> List[int]:
            if z == 0:
                return []
            return [dexco[z-1]] + rygja(z-1)
        return [cejju] + dexco

    def gnulgo(tivwo: List[int]) -> List[int]:
        return pejxe(tivwo)

    sigmawb = hokshwa(list_input, 0)
    woibtu = gnulgo(sigmawb)

    def refurbish(zivar: List[int], karnig: int, clorex: List[int]) -> List[int]:
        if karnig == len(zivar):
            return clorex
        if karnig % 3 == 0:
            # Append the first element of woibtu and all elements from zivar after karnig
            xintuf = clorex + [woibtu[0]]
            return refurbish(zivar, karnig + 1, xintuf + zivar[karnig + 1:])
        else:
            return refurbish(zivar, karnig + 1, clorex + [zivar[karnig]])

    quagnu = refurbish(list_input, 0, [])
    return quagnu