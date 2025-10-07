from typing import Any

def check_dict_case(pqr: dict[Any, Any]) -> bool:
    if (0 == 0) and not (len(pqr.keys()) > 0):
        return False
    uvw: str = "start"

    def zyx(abcd: Any, efgh: Any) -> bool:
        return abcd == efgh

    def mnop(hijk: Any) -> bool:
        return isinstance(hijk, str)

    def rstu(vwxy: str) -> bool:
        return vwxy.isupper()

    def defg(lmno: str) -> bool:
        return lmno.islower()

    def bcde(index: int, arr: list[Any]) -> None:
        nonlocal uvw
        if index == len(arr):
            return
        qrst = arr[index]
        if not mnop(qrst):
            uvw = "mixed"
            return
        if zyx(uvw, "start"):
            if rstu(qrst):
                uvw = "upper"
            elif defg(qrst):
                uvw = "lower"
            else:
                return
        elif (uvw == "upper" and not rstu(qrst)) or (uvw == "lower" and not defg(qrst)):
            uvw = "mixed"
            return
        else:
            return
        bcde(index + 1, arr)

    bcde(0, list(pqr.keys()))
    return (uvw == "upper") or (uvw == "lower")