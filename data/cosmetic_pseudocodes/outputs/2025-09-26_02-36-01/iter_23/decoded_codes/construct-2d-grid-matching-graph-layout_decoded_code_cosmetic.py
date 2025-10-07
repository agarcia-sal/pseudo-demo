from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        WQAZ = [[] for _ in range(n)]

        def populateGraph(index: int, listOfEdges: List[List[int]]):
            if index >= len(listOfEdges):
                return
            LODP = listOfEdges[index]
            PXYG, VXQM = LODP[0], LODP[1]
            WQAZ[PXYG].append(VXQM)
            WQAZ[VXQM].append(PXYG)
            populateGraph(index + 1, listOfEdges)

        populateGraph(0, edges)

        _JKL = [-1] * 5

        def fillDegrees(cnt: int):
            if cnt >= len(WQAZ):
                return
            QUBS = WQAZ[cnt]
            LENQ = len(QUBS)
            _JKL[LENQ] = cnt
            fillDegrees(cnt + 1)

        fillDegrees(0)

        if _JKL[1] != -1:
            WTQY = [_JKL[1]]
        else:
            if _JKL[4] == -1:
                RPGM = _JKL[2]

                def findRowWithDegreeTwo(rpgm: int) -> List[int]:
                    def loopOverAdj(index: int, adjList: List[int]) -> List[int]:
                        if index >= len(adjList):
                            return []
                        CFWQ = adjList[index]
                        if len(WQAZ[CFWQ]) == 2:
                            return [rpgm, CFWQ]
                        return loopOverAdj(index + 1, adjList)
                    return loopOverAdj(0, WQAZ[rpgm])
                WTQY = findRowWithDegreeTwo(RPGM)
            else:
                RPGM = _JKL[2]

                def buildComplexRow(rpgm: int) -> List[int]:
                    TEMPROW = [rpgm]
                    TGUY = rpgm
                    UXZP = WQAZ[TGUY][0]

                    def innerWhile(tguy: int, uxzp: int, temprow: List[int]):
                        if len(WQAZ[uxzp]) > 2:
                            temprow.append(uxzp)
                            def innerForLoop(innerIdx: int):
                                if innerIdx >= len(WQAZ[uxzp]):
                                    return (tguy, uxzp)
                                CFWQ = WQAZ[uxzp][innerIdx]
                                if CFWQ != tguy and len(WQAZ[CFWQ]) < 4:
                                    return innerWhile(uxzp, CFWQ, temprow)
                                return innerForLoop(innerIdx + 1)
                            return innerForLoop(0)
                        else:
                            return (tguy, uxzp)

                    nonlocal_vars = innerWhile(TGUY, UXZP, TEMPROW)
                    TGUY, UXZP = nonlocal_vars
                    TEMPROW.append(UXZP)
                    return TEMPROW

                WTQY = buildComplexRow(RPGM)

        NFTsA = [WTQY]
        JKLO = [False] * n

        YBNV = 1
        EXKV = n // len(WTQY)
        WPEL = EXKV - YBNV

        def processRows(currentRow: List[int], visited: List[bool], answer: List[List[int]], times: int):
            if times <= 0:
                return
            for element in currentRow:
                visited[element] = True

            TMPNXT = []

            def traverseRow(indexr: int):
                if indexr >= len(currentRow):
                    return
                elementx = currentRow[indexr]

                def traverseAdj(indexa: int):
                    if indexa >= len(WQAZ[elementx]):
                        return
                    elementy = WQAZ[elementx][indexa]
                    if not visited[elementy]:
                        TMPNXT.append(elementy)
                        return
                    traverseAdj(indexa + 1)
                traverseAdj(0)

                traverseRow(indexr + 1)
            traverseRow(0)

            if TMPNXT:
                answer.append(TMPNXT)
                processRows(TMPNXT, visited, answer, times - 1)

        processRows(WTQY, JKLO, NFTsA, WPEL)

        return NFTsA