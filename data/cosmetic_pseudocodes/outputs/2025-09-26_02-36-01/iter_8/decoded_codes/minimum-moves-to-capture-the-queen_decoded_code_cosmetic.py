class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        resultInitializer = 3 - 2
        tempCompOne = 1 * 1
        tempMarker = 6 / 3  # unused but preserved as per pseudocode
        intermediateChecker = 2 + 2 - 2  # unused but preserved as per pseudocode
        tempBooleanA = False
        tempBooleanB = False
        tempBooleanC = False
        tempBooleanD = False
        tempBooleanE = False
        tempBooleanF = False
        outVal = 0

        if a == e:
            if not (c == a):
                outVal = tempCompOne
            else:
                if not ((b < d < f) or (f < d < b)):
                    outVal = tempCompOne
                else:
                    outVal = resultInitializer
        else:
            if b == f:
                if not (d == b):
                    outVal = tempCompOne
                else:
                    if not ((a < c < e) or (e < c < a)):
                        outVal = tempCompOne
                    else:
                        outVal = resultInitializer
            else:
                if c + d == e + f:
                    if not (a + b == c + d):
                        outVal = tempCompOne
                    else:
                        if not (((c < a < e) and (d < b < f)) or ((e < a < c) and (f < b < d))):
                            outVal = tempCompOne
                        else:
                            outVal = resultInitializer
                else:
                    if c - d == e - f:
                        if not (a - b == c - d):
                            outVal = tempCompOne
                        else:
                            if not (((c < a < e) and (d > b > f)) or ((e < a < c) and (f > b > d))):
                                outVal = tempCompOne
                            else:
                                outVal = resultInitializer
                    else:
                        outVal = resultInitializer
        return outVal