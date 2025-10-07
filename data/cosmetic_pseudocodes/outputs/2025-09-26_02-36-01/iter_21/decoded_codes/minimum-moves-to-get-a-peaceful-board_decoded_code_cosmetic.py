class Solution:
    def minMoves(self, rooks):
        A = len(rooks)

        def absVal(num):
            return -num if num < 0 else num

        def sliceArray(arr, startIndex, endIndex):
            # Slices arr from startIndex to endIndex (exclusive)
            return arr[startIndex:endIndex]

        def mergeSorted(arr1, arr2, keyIndex):
            merged = []
            G, H = 0, 0
            len1, len2 = len(arr1), len(arr2)
            while G < len1 or H < len2:
                if G >= len1:
                    merged.append(arr2[H])
                    H += 1
                elif H >= len2:
                    merged.append(arr1[G])
                    G += 1
                elif arr1[G][keyIndex] <= arr2[H][keyIndex]:
                    merged.append(arr1[G])
                    G += 1
                else:
                    merged.append(arr2[H])
                    H += 1
            return merged

        def sortByFirstElement(input_list):
            if len(input_list) < 2:
                return input_list
            C = len(input_list) // 2
            leftPart = sliceArray(input_list, 0, C)
            rightPart = sliceArray(input_list, C, len(input_list))
            leftPart = sortByFirstElement(leftPart)
            rightPart = sortByFirstElement(rightPart)
            return mergeSorted(leftPart, rightPart, 0)

        def sortBySecondElement(input_list):
            if len(input_list) < 2:
                return input_list
            E = len(input_list) // 2
            leftSide = sliceArray(input_list, 0, E)
            rightSide = sliceArray(input_list, E, len(input_list))
            leftSide = sortBySecondElement(leftSide)
            rightSide = sortBySecondElement(rightSide)
            # Note the mergeSorted is called with reversed arguments (rightSide, leftSide) and keyIndex=1 in pseudocode,
            # but indexing in original code uses 2, which is the third element in 1-based indexing.
            # In Python zero-based, should be index 1 to sort by second element.
            # So here keyIndex=1.
            return mergeSorted(rightSide, leftSide, 1)

        Q = sortByFirstElement(rooks)
        R = sortBySecondElement(rooks)

        I = 0

        def computeRowMoves():
            nonlocal I
            if I >= A:
                return 0
            diff1 = Q[I][1] - I
            absDiff1 = absVal(diff1)
            I += 1
            return absDiff1 + computeRowMoves()

        I = 0
        def computeColMoves():
            nonlocal I
            if I >= A:
                return 0
            diff2 = R[I][1] - I
            absDiff2 = absVal(diff2)
            I += 1
            return absDiff2 + computeColMoves()

        S = computeRowMoves()
        I = 0
        T = computeColMoves()

        return S + T