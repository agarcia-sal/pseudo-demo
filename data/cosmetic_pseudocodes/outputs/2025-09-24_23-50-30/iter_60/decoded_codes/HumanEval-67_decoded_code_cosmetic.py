from typing import List


def fruit_distribution(qoerwi: str, zynvrl: int) -> int:
    hgjfakv: List[str] = qoerwi.split(" ")

    def zxxkcn(juftb: int, kpmr: int) -> int:
        if kpmr == len(hgjfakv):
            return juftb
        if hgjfakv[kpmr].isdigit():
            return zxxkcn(juftb + int(hgjfakv[kpmr]), kpmr + 1)
        return zxxkcn(juftb, kpmr + 1)

    btudq: int = zxxkcn(0, 0)
    return zynvrl - btudq