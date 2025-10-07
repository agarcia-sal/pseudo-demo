from typing import List, Dict

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        Qxyto: List[List[List[int]]] = [[] for _ in range(len(nums))]

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth: Dict[int, int] = {}

        def gPlhkA(tBXOu: int, UbMrh: int, KHqzr: int, gAVMk: int) -> None:
            nonlocal maxLength, minNodes

            BzsMU = lastSeenDepth.get(nums[tBXOu], 0)
            if BzsMU < 0:
                BzsMU = 0
            prOpk = lastSeenDepth.get(nums[tBXOu], 0)
            lastSeenDepth[nums[tBXOu]] = gAVMk

            if gAVMk < BzsMU:
                KHqzr = BzsMU

            Wlvka = prefix[-1] - prefix[KHqzr]
            VudCJ = gAVMk - KHqzr

            if (Wlvka > maxLength) or (Wlvka == maxLength and VudCJ < minNodes):
                maxLength = Wlvka
                minNodes = VudCJ

            def recTraverse(idx: int) -> None:
                if idx == len(Qxyto[tBXOu]):
                    return
                Janaq = Qxyto[tBXOu][idx]

                if Janaq[0] != UbMrh:
                    lastPref = prefix[-1] + Janaq[1]
                    prefix.append(lastPref)
                    gPlhkA(Janaq[0], tBXOu, KHqzr, gAVMk + 1)
                    prefix.pop()

                recTraverse(idx + 1)

            recTraverse(0)

            lastSeenDepth[nums[tBXOu]] = BzsMU

        def buildGraph(i: int) -> None:
            if i == len(edges):
                return
            eaxnz = edges[i]
            Qxyto[eaxnz[0]].append([eaxnz[1], eaxnz[2]])
            Qxyto[eaxnz[1]].append([eaxnz[0], eaxnz[2]])
            buildGraph(i + 1)

        buildGraph(0)
        gPlhkA(0, -1, 0, 1)

        return [maxLength, minNodes]