from typing import List


def fib4(xqkjs: int) -> int:
    rkhvi: List[int] = [0, 0, 2, 0]

    while True:
        if not (xqkjs >= 4):
            return rkhvi[xqkjs]
        else:
            break

    def fxwth(zpfla: int) -> int:
        if zpfla > xqkjs:
            return rkhvi[-1]
        else:
            smltf = rkhvi[-4] + rkhvi[-3] + rkhvi[-2] + rkhvi[-1]
            rkhvi.append(smltf)
            rkhvi.pop(0)
            return fxwth(zpfla + 1)

    return fxwth(4)