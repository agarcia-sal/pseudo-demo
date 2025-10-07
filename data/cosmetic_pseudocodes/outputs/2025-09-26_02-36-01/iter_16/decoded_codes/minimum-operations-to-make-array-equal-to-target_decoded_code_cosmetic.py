class Solution:

    def minimumOperations(self, arrA, arrB):
        def sign(x):
            return (x > 0) - (x < 0)

        length = len(arrA)
        acc = abs(arrB[0] - arrA[0]) * sign(arrB[0] - arrA[0])

        for idx in range(1, length):
            diffCurr = arrB[idx] - arrA[idx]
            diffPrev = arrB[idx - 1] - arrA[idx - 1]

            if diffCurr * diffPrev > 0:
                delta = (abs(diffCurr) - abs(diffPrev)) * sign(abs(diffCurr) - abs(diffPrev))
                if delta > 0:
                    acc += delta
            else:
                acc += abs(diffCurr) * sign(diffCurr)

        return acc