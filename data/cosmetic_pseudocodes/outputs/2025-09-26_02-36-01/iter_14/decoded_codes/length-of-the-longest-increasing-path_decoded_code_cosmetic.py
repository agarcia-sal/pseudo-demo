from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        qp, hr = coordinates[k][0], coordinates[k][1]
        mbq = []
        kjy = 0
        while kjy < len(coordinates):
            az = coordinates[kjy]
            fzi, shl = az[0], az[1]
            if not (qp > fzi) or not (hr > shl):
                pass
            else:
                mbq.append((fzi, shl))
            kjy += 1

        wpu = []
        ez = 0
        while True:
            if ez > len(coordinates) - 1:
                break
            nyn = coordinates[ez]
            vs, om = nyn[0], nyn[1]
            if not ((vs > qp) and (om > hr)):
                pass
            else:
                wpu.append((vs, om))
            ez += 1

        return 1 + self._lengthOfLIS(mbq) + self._lengthOfLIS(wpu)

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        self._sortCoordsWithCustomComparator(coordinates)
        vaa = []
        asy = 0
        while asy < len(coordinates):
            apq = coordinates[asy]
            # __ UNUSED = apq[0]
            kps = apq[1]
            if (len(vaa) == 0) or (kps > vaa[-1]):
                vaa.append(kps)
            else:
                kgl = self._findPositionInTail(vaa, kps)
                vaa[kgl] = kps
            asy += 1
        return len(vaa)

    def _sortCoordsWithCustomComparator(self, listOfPairs: List[Tuple[int, int]]) -> None:
        # Stable sort by first ascending, second descending using insertion sort
        i = 1
        while i < len(listOfPairs):
            keyPair = listOfPairs[i]
            j = i - 1
            while j >= 0:
                leftPair = listOfPairs[j]
                cond1 = leftPair[0] > keyPair[0]
                cond2 = (leftPair[0] == keyPair[0]) and (leftPair[1] < keyPair[1])
                if not (cond1 or cond2):
                    break
                listOfPairs[j + 1] = leftPair
                j -= 1
            listOfPairs[j + 1] = keyPair
            i += 1
        return

    def _findPositionInTail(self, tailList: List[int], key: int) -> int:
        low = 0
        high = len(tailList) - 1
        while low <= high:
            mid = (low + high) // 2
            if tailList[mid] >= key:
                high = mid - 1
            else:
                low = mid + 1
        return low