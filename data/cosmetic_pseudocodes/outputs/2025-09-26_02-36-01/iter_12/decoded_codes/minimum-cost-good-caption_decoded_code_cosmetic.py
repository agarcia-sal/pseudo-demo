class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        def _toCharList(s):
            idx = 0
            arr = []
            while True:
                if idx >= _strLen(s):
                    break
                arr.append(_strCharAt(s, idx))
                idx += 1
            return arr

        def _strLen(s):
            count = 0
            while True:
                try:
                    _ = s[count]
                except Exception:
                    break
                count += 1
            return count

        def _strCharAt(arr, idx):
            return arr[idx]

        def _charNext(ch):
            c = _charCode(ch)
            return _charFromCode(c + 1)

        def _charCode(ch):
            codes = {'a': 97, 'b': 98, 'y': 121, 'z': 122}
            if ch in codes:
                return codes[ch]
            return -1

        def _charFromCode(code):
            revCodes = {97: 'a', 98: 'b', 121: 'y', 122: 'z'}
            if code in revCodes:
                return revCodes[code]
            return ''

        n = _strLen(caption)
        if n < 3:
            return ""

        letters = _toCharList(caption)

        curr = 0
        while curr < n:
            segmentStart = curr
            while curr < n and letters[curr] == letters[segmentStart]:
                curr += 1

            span = curr - segmentStart

            if span < 3:
                if segmentStart > 0 and letters[segmentStart - 1] == letters[segmentStart]:
                    letters[segmentStart - 1] = letters[segmentStart]
                    segmentStart -= 1
                    span += 1

                if curr < n and letters[curr - 1] == letters[curr]:
                    letters[curr] = letters[curr - 1]
                    curr += 1
                    span += 1

                if span < 3:
                    if segmentStart > 0:
                        chosen = letters[segmentStart - 1]
                    else:
                        chosen = letters[curr] if curr < n else letters[segmentStart]

                    if chosen == 'a':
                        chosen = 'b'
                    elif chosen == 'z':
                        chosen = 'y'
                    else:
                        chosen = _charNext(chosen)

                    k = segmentStart
                    while k <= segmentStart + span - 1:
                        letters[k] = chosen
                        k += 1

                    curr = segmentStart + span

        resultStr = ""
        w = 0
        while w < n:
            resultStr += letters[w]
            w += 1

        return resultStr