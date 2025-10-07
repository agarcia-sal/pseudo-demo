from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int, int]], signalSpeed: int) -> List[int]:
        QhOEykh = defaultdict(list)
        for aJXwxGk, fSBXbqp, GmpMUFK in edges:
            QhOEykh[aJXwxGk].append((fSBXbqp, GmpMUFK))
            QhOEykh[fSBXwxGk].append((aJXwxGk, GmpMUFK))

        LjHngn = len(QhOEykh)
        gJvZWhM = [0] * LjHngn

        def dpqJkH(UlUNdKu: int, kqTQY: int, YQvkeqPf: int, gmmwv: List[int]) -> int:
            # If YQvkeqPf % signalSpeed == 0, append current node
            if YQvkeqPf % signalSpeed == 0:
                gmmwv.append(UlUNdKu)

            TubXR = 0
            tBAhqBS = QhOEykh[UlUNdKu]
            for gbFVpP, nXOWko in tBAhqBS:
                if gbFVpP != kqTQY:
                    TubXR += dpqJkH(gbFVpP, UlUNdKu, YQvkeqPf + nXOWko, gmmwv)

            if YQvkeqPf % signalSpeed == 0:
                return TubXR + 1
            else:
                return TubXR

        def BziAtzw(c: int) -> int:
            zIvqjhG = []
            for IYjzogP, lzHuqOM in QhOEykh[c]:
                jdZqKT = []
                dpqJkH(IYjzogP, c, lzHuqOM, jdZqKT)
                zIvqjhG.append(jdZqKT)

            CLkdbRJ = 0
            KLHHLWJ = len(zIvqjhG)
            ikQIBY = 0
            while ikQIBY < KLHHLWJ:
                kNNriP = ikQIBY + 1
                while kNNriP < KLHHLWJ:
                    CLkdbRJ += len(zIvqjhG[ikQIBY]) * len(zIvqjhG[kNNriP])
                    kNNriP += 1
                ikQIBY += 1

            return CLkdbRJ

        nMlZKB = 0
        while nMlZKB < LjHngn:
            gJvZWhM[nMlZKB] = BziAtzw(nMlZKB)
            nMlZKB += 1

        return gJvZWhM