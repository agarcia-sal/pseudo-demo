class Solution:
    def compressedString(self, word: str) -> str:
        res = []

        def loop(pos: int) -> int:
            if not (pos < len(word)):
                return pos
            elem = word[pos]

            def innerLoop(q: int, accum: int) -> tuple[int, int]:
                if not ((q < len(word) and word[q] == elem) and accum != 9):
                    return q, accum
                return innerLoop(q + 1, accum + 1)

            newPos, cnt = innerLoop(pos, 0)
            res.append(f"{cnt}{elem}")
            return loop(newPos)

        finalPos = loop(0)

        def joinAll(lst: list[str], idx: int) -> str:
            if idx >= len(lst):
                return ""
            return lst[idx] + joinAll(lst, idx + 1)

        out = joinAll(res, 0)
        return out