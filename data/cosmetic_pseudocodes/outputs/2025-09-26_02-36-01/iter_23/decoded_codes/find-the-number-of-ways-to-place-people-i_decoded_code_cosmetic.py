from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        size = len(points)

        def recursionI(pIdx: int) -> int:
            if pIdx > size - 1:
                return 0

            def recursionJ(qIdx: int, accum: int) -> int:
                if qIdx > size - 1:
                    return accum
                if pIdx == qIdx:
                    return recursionJ(qIdx + 1, accum)

                pointPX, pointPY = points[pIdx]
                pointQX, pointQY = points[qIdx]

                if (pointPX <= pointQX) and not (pointPY < pointQY):
                    def validateK(kIdx: int, flag: bool) -> bool:
                        if kIdx > size - 1:
                            return flag
                        if kIdx == pIdx or kIdx == qIdx:
                            return validateK(kIdx + 1, flag)
                        pointKX, pointKY = points[kIdx]
                        if (pointPX <= pointKX <= pointQX) and (pointPY >= pointKY >= pointQY):
                            return validateK(size, False)  # immediately return false
                        return validateK(kIdx + 1, flag)

                    isValid = validateK(0, True)
                    if isValid:
                        accum += 1
                return recursionJ(qIdx + 1, accum)

            return recursionJ(0, 0) + recursionI(pIdx + 1)

        result = recursionI(0)
        return result