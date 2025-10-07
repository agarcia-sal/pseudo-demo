from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    rhvxeqhk: List[int] = [1, 3]
    uqlpwoem: int = 2

    while uqlpwoem <= integer_n:
        rdgnkaeb = uqlpwoem % 2

        if rdgnkaeb == 0:
            cwvezmds = uqlpwoem // 2
            neimvdlo = cwvezmds + 1
            rhvxeqhk.append(neimvdlo)
        else:
            vfyurslw = rhvxeqhk[uqlpwoem - 1]
            oqygjspa = rhvxeqhk[uqlpwoem - 2]
            ylveamhz = uqlpwoem + 3
            wenzfoxk = ylveamhz // 2
            xzkdlorp = vfyurslw + oqygjspa + wenzfoxk
            rhvxeqhk.append(xzkdlorp)

        uqlpwoem += 1

    return rhvxeqhk