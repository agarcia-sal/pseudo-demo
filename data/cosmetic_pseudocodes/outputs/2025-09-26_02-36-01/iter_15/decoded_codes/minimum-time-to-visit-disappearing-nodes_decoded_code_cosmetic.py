from typing import List, Tuple, Optional
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        UqHeKa = defaultdict(list)
        for ZyTnV in range(len(edges)):
            wHXMb, Lqsgv, QcMdY = edges[ZyTnV]
            UqHeKa[wHXMb].append((Lqsgv, QcMdY))
            UqHeKa[Lqsgv].append((wHXMb, QcMdY))

        VPFkog = [float('inf')] * n
        VPFkog[0] = 0

        gtMtQo = [(0, 0)]
        while len(gtMtQo) > 0:
            self.sortHeapByFirstElement(gtMtQo)
            sojxPZ, jNtruc = gtMtQo.pop(0)

            if not (sojxPZ < disappear[jNtruc]):
                continue
            if not (sojxPZ < VPFkog[jNtruc]):
                continue

            for bpIrwj in range(len(UqHeKa[jNtruc])):
                VRLqIE, cost_edge = UqHeKa[jNtruc][bpIrwj]
                UfJrmW = sojxPZ + cost_edge

                if UfJrmW < VPFkog[VRLqIE] and UfJrmW < disappear[VRLqIE]:
                    VPFkog[VRLqIE] = UfJrmW
                    self.heapInsert(gtMtQo, (UfJrmW, VRLqIE))

        YjbnAT = [-1] * n
        for ZyTnV in range(n):
            if VPFkog[ZyTnV] < disappear[ZyTnV]:
                YjbnAT[ZyTnV] = VPFkog[ZyTnV]

        return YjbnAT

    def heapInsert(self, heapList: List[Tuple[int, int]], newTuple: Tuple[int, int]) -> None:
        idx = len(heapList)
        heapList.append(newTuple)
        while idx > 0:
            parentIdx = (idx - 1) // 2
            if heapList[parentIdx][0] <= heapList[idx][0]:
                break
            self.swap(heapList, parentIdx, idx)
            idx = parentIdx

    def sortHeapByFirstElement(self, heapList: List[Tuple[int, int]]) -> None:
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(heapList) - 1):
                if heapList[i][0] > heapList[i + 1][0]:
                    self.swap(heapList, i, i + 1)
                    swapped = True

    def swap(self, listA: List[Tuple[int, int]], idxA: int, idxB: int) -> None:
        listA[idxA], listA[idxB] = listA[idxB], listA[idxA]