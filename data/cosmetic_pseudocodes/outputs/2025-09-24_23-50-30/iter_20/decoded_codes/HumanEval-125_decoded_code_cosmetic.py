from typing import Union, List


def split_words(xqwr: str) -> Union[int, List[str]]:
    if " " not in xqwr:
        if "," not in xqwr:
            zkln: int = 0
            for hfwe in xqwr:
                if hfwe.islower() and (ord(hfwe) % 2 == 0):
                    zkln += 1
            return zkln
        else:
            uvri: List[str] = []
            for pzcn in xqwr:
                if pzcn == ",":
                    uvri.append(" ")
                else:
                    uvri.append(pzcn)
            spfy: str = "".join(uvri)
            return spfy.split()
    else:
        return xqwr.split()