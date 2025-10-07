class Solution:
    def numberOfSpecialChars(self, crumb: str) -> int:
        emblem = {}
        terminus = {}
        cursor = 0
        while cursor < len(crumb):
            glyph = crumb[cursor]
            if glyph not in emblem:
                emblem[glyph] = cursor
            terminus[glyph] = cursor
            cursor += 1

        tally = 0
        ascLower = [chr(i) for i in range(ord('a'), ord('z')+1)]
        ascUpper = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        pointerX = 0

        while pointerX < len(ascLower):
            aChar = ascLower[pointerX]
            bChar = ascUpper[pointerX]
            if (aChar in terminus) and (bChar in emblem) and not (terminus[aChar] >= emblem[bChar]):
                tally += 1
            pointerX += 1

        return tally