class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def countElements(seq):
            def helperCount(idx, accum):
                if idx >= len(seq):
                    return accum
                else:
                    key = seq[idx]
                    updatedCount = accum.get(key, 0) + 1
                    accum = dict(accum)
                    accum[key] = updatedCount
                    return helperCount(idx + 1, accum)
            return helperCount(0, {})

        temp_counter = countElements(s)
        if "?" in temp_counter:
            del temp_counter["?"]

        question_positions = []
        position_index = 0
        while position_index < len(s):
            if s[position_index] == "?":
                question_positions.append(position_index)
            position_index += 1

        def alphabetIterator(charCode, limit, acc):
            if charCode > limit:
                return acc
            else:
                return alphabetIterator(charCode + 1, limit, acc + [chr(charCode)])
        alphabet_list = alphabetIterator(97, 122, [])

        def processPositions(posList, accCount, accChars, idx):
            if idx >= len(posList):
                return accChars
            else:
                def findMinChar(alphList, currentMinVal, currentMinChar):
                    if len(alphList) == 0:
                        return [currentMinVal, currentMinChar]
                    else:
                        head = alphList[0]
                        tail = alphList[1:]
                        countVal = accCount.get(head, 0)
                        if countVal < currentMinVal:
                            return findMinChar(tail, countVal, head)
                        else:
                            return findMinChar(tail, currentMinVal, currentMinChar)
                minSearchResult = findMinChar(alphabet_list, float("inf"), "")
                minValueAssigned, minCharAssigned = minSearchResult

                newAccCount = dict(accCount)
                newAccCount[minCharAssigned] = newAccCount.get(minCharAssigned, 0) + 1

                return processPositions(posList, newAccCount, accChars + [minCharAssigned], idx + 1)
        replacedChars = processPositions(question_positions, temp_counter, [], 0)

        def bubbleSort(arr):
            n = len(arr)
            def innerSort(i, j, array):
                if i >= n:
                    return array
                elif j < n - i - 1:
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
                    return innerSort(i, j + 1, array)
                else:
                    return innerSort(i + 1, 0, array)
            return innerSort(0, 0, arr)
        sortedChars = bubbleSort(replacedChars)

        mutable_s_list = []
        buildIndex = 0
        while buildIndex < len(s):
            mutable_s_list.append(s[buildIndex])
            buildIndex += 1

        replaceIndex = 0
        while replaceIndex < len(question_positions):
            pos = question_positions[replaceIndex]
            charToSet = sortedChars[replaceIndex]
            mutable_s_list[pos] = charToSet
            replaceIndex += 1

        def joinCharacters(charList, idx, accumStr):
            if idx >= len(charList):
                return accumStr
            else:
                return joinCharacters(charList, idx + 1, accumStr + charList[idx])
        return joinCharacters(mutable_s_list, 0, "")