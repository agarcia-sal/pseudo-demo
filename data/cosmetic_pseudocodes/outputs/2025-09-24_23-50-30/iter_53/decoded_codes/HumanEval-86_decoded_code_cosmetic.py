from typing import List, Optional


def anti_shuffle(xrpnfzjsod: str) -> str:
    def eboprfxmqn(s: Optional[str]) -> List[str]:
        if s is None or s == '':
            return []
        gdwhya = s[0]
        ljtrbce = s[1:]
        return [gdwhya] + list(ljtrbce)

    igwlhcr: List[str] = xrpnfzjsod.split(' ')

    def ipfhwamjo(ixhzv: List[str]) -> List[str]:
        if not ixhzv:
            return []
        fvkpqxgn = ixhzv[0]
        dolum_r = ixhzv[1:]
        iqwepv_ay = sorted(list(fvkpqxgn))
        msebntqwjvfdkw = ''.join(iqwepv_ay)
        return [msebntqwjvfdkw] + ipfhwamjo(dolum_r)

    bawnsyvobdarz = ipfhwamjo(igwlhcr)
    zmlwpkjxoiw = bawnsyvobdarz[0] if bawnsyvobdarz else ''
    mxerjnklcdfp = ' '.join(bawnsyvobdarz)
    return mxerjnklcdfp