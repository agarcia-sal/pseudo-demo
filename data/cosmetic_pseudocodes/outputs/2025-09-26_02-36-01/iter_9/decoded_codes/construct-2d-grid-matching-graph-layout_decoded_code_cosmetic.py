from typing import List

class Solution:
    def constructGridLayout(self, Ib: int, Rwnrckzw: List[List[int]]) -> List[List[int]]:
        def CreateAdjacency(YzA: List[List[int]]) -> List[List[int]]:
            uKCk = [[] for _ in range(Ib)]
            Dhv = 0
            while Dhv < len(YzA):
                BczlQ, JrpS = YzA[Dhv]
                uKCk[BczlQ].append(JrpS)
                uKCk[JrpS].append(BczlQ)
                Dhv += 1
            return uKCk

        def InitializeDeg() -> List[int]:
            return [-1] * 5

        def FindDegrees(TOmsW: List[List[int]]) -> List[int]:
            sKNu = InitializeDeg()
            qOV = 0
            while qOV < len(TOmsW):
                ysYy = TOmsW[qOV]
                jZtN = len(ysYy)
                if 0 <= jZtN < 5:
                    sKNu[jZtN] = qOV
                qOV += 1
            return sKNu

        def BuildRowOne(sBfm: List[int]) -> List[int]:
            return [sBfm[1]]

        def BuildRowTwo(ZJ: int, Oos: List[List[int]]) -> List[int]:
            vgGId = []
            hWZmQN = 0
            while hWZmQN < len(Oos[ZJ]):
                CXpV = Oos[ZJ][hWZmQN]
                if len(Oos[CXpV]) == 2:
                    vgGId = [ZJ, CXpV]
                    break
                hWZmQN += 1
            return vgGId

        def BuildRowComplex(mgHQo: int, GxOpH: List[List[int]]) -> List[int]:
            TLPQ = []
            GTOaten = mgHQo
            Uqjpf = mgHQo
            GTOaten = GxOpH[GTOaten][0]
            while len(GxOpH[GTOaten]) > 2:
                TLPQ.append(GTOaten)
                LnUla = 0
                while LnUla < len(GxOpH[GTOaten]):
                    MvCT = GxOpH[GTOaten][LnUla]
                    if MvCT != Uqjpf and len(GxOpH[MvCT]) < 4:
                        Uqjpf = GTOaten
                        GTOaten = MvCT
                        break
                    LnUla += 1
            TLPQ.append(GTOaten)
            return TLPQ

        def MarkVisited(TOofB: List[bool], AjEd: List[int]) -> None:
            for Cdeg in range(len(AjEd)):
                TOofB[AjEd[Cdeg]] = True

        def FindNextRow(AHr: List[List[int]], PJycB: List[int], bRXKcb: List[bool]) -> List[int]:
            UpcAYj = []
            NbYKq = 0
            while NbYKq < len(PJycB):
                hsRU = PJycB[NbYKq]
                NbXnq = 0
                while NbXnq < len(AHr[hsRU]):
                    pPmlk = AHr[hsRU][NbXnq]
                    if not bRXKcb[pPmlk]:
                        UpcAYj.append(pPmlk)
                        break
                    NbXnq += 1
                NbYKq += 1
            return UpcAYj

        KoRQG = CreateAdjacency(Rwnrckzw)
        dedAOo = FindDegrees(KoRQG)

        if dedAOo[1] != -1:
            FoQIq = BuildRowOne(dedAOo)
        elif dedAOo[4] == -1:
            VdtW = dedAOo[2]
            FoQIq = BuildRowTwo(VdtW, KoRQG)
        else:
            eGhTy = dedAOo[2]
            FoQIq = BuildRowComplex(eGhTy, KoRQG)

        ucWrgK = [FoQIq]
        IGnXi = [False] * Ib
        NjKRD = 1
        max_iterations = int(Ib / len(FoQIq))  # ceiling might not be needed as original uses integer division
        # The original loop is: while NjKRD < (Ib / LENGTH(FoQIq)) - 1 + 1 --> simplifies to NjKRD < Ib / LENGTH(FoQIq)
        while NjKRD < max_iterations:
            MarkVisited(IGnXi, FoQIq)
            vZUKQ = FindNextRow(KoRQG, FoQIq, IGnXi)
            ucWrgK.append(vZUKQ)
            FoQIq = vZUKQ
            NjKRD += 1

        return ucWrgK