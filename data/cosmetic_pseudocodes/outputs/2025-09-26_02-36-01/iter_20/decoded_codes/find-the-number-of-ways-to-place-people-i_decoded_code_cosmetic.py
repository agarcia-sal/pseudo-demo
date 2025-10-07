from typing import List, Tuple

class Solution:
    def numberOfPairs(self, points: List[Tuple[int, int]]) -> int:
        def getX(idx: int) -> int:
            return points[idx][0]

        def getY(idx: int) -> int:
            return points[idx][1]

        def checkInsideBounds(aX: int, bX: int, cX: int, aY: int, bY: int, cY: int) -> bool:
            return (aX <= bX) and (bX <= cX) and (aY >= bY) and (bY >= cY)

        alpha = 0
        beta = len(points)

        def outerLoop(m: int) -> None:
            nonlocal alpha
            if m >= beta:
                return

            def innerLoop(n: int) -> None:
                nonlocal alpha
                if n >= beta:
                    return

                if m != n:
                    sX = getX(m)
                    sY = getY(m)
                    tX = getX(n)
                    tY = getY(n)

                    if (sX <= tX) and (sY >= tY):
                        omega = True

                        def middleCheck(p: int) -> None:
                            nonlocal omega
                            if p >= beta:
                                return

                            if (p != m) and (p != n):
                                uX = getX(p)
                                uY = getY(p)

                                if checkInsideBounds(sX, uX, tX, sY, uY, tY):
                                    omega = False
                                    return
                            # Continue checking further points only if omega still True
                            if omega:
                                middleCheck(p + 1)

                        middleCheck(0)

                        if omega:
                            alpha += 1

                innerLoop(n + 1)

            innerLoop(0)
            outerLoop(m + 1)

        outerLoop(0)
        return alpha