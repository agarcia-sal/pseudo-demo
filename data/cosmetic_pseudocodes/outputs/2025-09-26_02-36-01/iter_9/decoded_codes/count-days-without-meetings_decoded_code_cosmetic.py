class Solution:
    def countDays(self, gamma, delta):
        def swapSigma(arr, x, y):
            arr[x], arr[y] = arr[y], arr[x]

        def partitionPi(arr, low, high):
            pivot = arr[high][0]
            i = low - 1
            for j in range(low, high):
                if arr[j][0] <= pivot:
                    i += 1
                    swapSigma(arr, i, j)
            swapSigma(arr, i + 1, high)
            return i + 1

        def quickSortTheta(e, a, b):
            if a < b:
                pIndex = partitionPi(e, a, b)
                quickSortTheta(e, a, pIndex - 1)
                quickSortTheta(e, pIndex + 1, b)

        quickSortTheta(delta, 0, len(delta) - 1)

        omega = 1
        phi = 0

        def processMeeting(zet):
            nonlocal omega, phi
            alpha = zet[0]
            beta = zet[1]
            if omega < alpha:
                phi += alpha - omega
            if omega <= beta:
                omega = beta + 1

        kappa = 0
        while kappa < len(delta):
            processMeeting(delta[kappa])
            kappa += 1

        if omega <= gamma:
            phi += gamma - omega + 1

        return phi