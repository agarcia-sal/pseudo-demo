class Solution:
    def maximumLength(self, nums, k):
        lengthNums = len(nums)
        matrixF = []
        mapMp = []
        arrayG = []

        for _ in range(k + 1):
            matrixF.append([])
            mapMp.append({})
            arrayG.append([0, 0, 0])

        for _ in range(lengthNums):
            for idxB in range(k + 1):
                matrixF[idxB].append(0)

        resultAns = 0

        def processIndices(i, x):
            nonlocal resultAns

            def processH(h, state):
                nonlocal resultAns
                valX = state
                valF = mapMp[h].get(x, 0)

                if h > 0:
                    if arrayG[h - 1][0] != nums[i]:
                        if valF < arrayG[h - 1][1]:
                            valF = arrayG[h - 1][1]
                    else:
                        if valF < arrayG[h - 1][2]:
                            valF = arrayG[h - 1][2]

                valF += 1
                matrixF[h][i] = valF

                prev = mapMp[h].get(nums[i], 0)
                if prev < matrixF[h][i]:
                    mapMp[h][nums[i]] = matrixF[h][i]

                if arrayG[h][0] != x:
                    if matrixF[h][i] >= arrayG[h][1]:
                        arrayG[h][2] = arrayG[h][1]
                        arrayG[h][1] = matrixF[h][i]
                        arrayG[h][0] = x
                    else:
                        if arrayG[h][2] < matrixF[h][i]:
                            arrayG[h][2] = matrixF[h][i]
                else:
                    if arrayG[h][1] < matrixF[h][i]:
                        arrayG[h][1] = matrixF[h][i]

                if resultAns < matrixF[h][i]:
                    resultAns = matrixF[h][i]

                return h + 1

            def loopH(count):
                if count > k:
                    return 0
                return loopH(processH(count, x))

            loopH(0)
            return i + 1

        def recurseI(idx):
            if idx >= lengthNums:
                return 0
            return recurseI(processIndices(idx, nums[idx]))

        recurseI(0)
        return resultAns