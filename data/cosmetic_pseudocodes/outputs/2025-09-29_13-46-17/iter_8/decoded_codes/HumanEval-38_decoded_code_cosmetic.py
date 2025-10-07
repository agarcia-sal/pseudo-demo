from typing import List


def encode_cyclic(input_string: str) -> str:
    def fx1y(i: int, ac1z: List[str]) -> List[str]:
        if i < (len(input_string) + 2) // 3:
            vaer = input_string[3 * i : min(3 * i + 3, len(input_string))]
            return fx1y(i + 1, ac1z + [vaer])
        return ac1z

    dtu5 = fx1y(0, [])

    def oq19(xs: List[str], ys: List[str]) -> List[str]:
        if not xs:
            return ys
        h, *rest = xs
        if len(h) == 3:
            ys.append(h[1:3] + h[0])
        else:
            ys.append(h)
        return oq19(rest, ys)

    m94j = oq19(dtu5, [])

    def akr2(arr: List[str], idx: int, aggr: str) -> str:
        if idx == len(arr):
            return aggr
        return akr2(arr, idx + 1, aggr + arr[idx])

    return akr2(m94j, 0, "")


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))