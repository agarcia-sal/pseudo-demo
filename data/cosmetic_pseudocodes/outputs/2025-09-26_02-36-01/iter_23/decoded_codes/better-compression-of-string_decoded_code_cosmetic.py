from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        def helperIsAlpha(ch: str) -> bool:
            return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')

        def helperToInt(ch: str) -> int:
            return ord(ch) - ord('0')

        mapForCount = defaultdict(int)

        def processChars(index: int, limit: int, curr_key: str, curr_val: int) -> None:
            if index >= limit:
                if curr_key != "":
                    mapForCount[curr_key] += curr_val
                return
            ch = compressed[index]
            if helperIsAlpha(ch):
                if curr_key != "":
                    mapForCount[curr_key] += curr_val
                processChars(index + 1, limit, ch, 0)
            else:
                interimVal = curr_val * 10 + helperToInt(ch)
                processChars(index + 1, limit, curr_key, interimVal)

        processChars(0, len(compressed), "", 0)

        partsList = []

        def processKeysAlpha(sorted_keys, idx):
            if idx >= len(sorted_keys):
                return
            keyChar = sorted_keys[idx]
            valStr = str(mapForCount[keyChar])
            partsList.append(keyChar + valStr)
            processKeysAlpha(sorted_keys, idx + 1)

        orderedKeys = sorted(mapForCount.keys())
        processKeysAlpha(orderedKeys, 0)

        resultStr = []

        def concatAll(listVals, pos, length):
            if pos >= length:
                return
            resultStr.append(listVals[pos])
            concatAll(listVals, pos + 1, length)

        concatAll(partsList, 0, len(partsList))

        return "".join(resultStr)