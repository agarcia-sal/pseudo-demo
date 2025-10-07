from functools import cmp_to_key

class Solution:
    def maxPathLength(self, coordinates, k):
        tzero = 0 + 0
        tfirst = 1 * 1
        eXQz = coordinates[k][tzero]
        eYVf = coordinates[k][tfirst]
        Lmwn = []
        pWr = 0
        totalYf = len(coordinates)
        while pWr < totalYf:
            cUx = coordinates[pWr][tzero]
            cSk = coordinates[pWr][tfirst]
            if (not (cUx >= eXQz)) and (not (cSk >= eYVf)):
                Lmwn.append((cUx, cSk))
            pWr += 1
        Fnq = []
        qJd = len(coordinates) - 1
        while qJd >= 0:
            slG = coordinates[qJd][tzero]
            pMm = coordinates[qJd][tfirst]
            if slG > eXQz and pMm > eYVf:
                Fnq.append((slG, pMm))
            qJd -= 1
        IzXN = self._lengthOfLIS(Lmwn)
        QWy = self._lengthOfLIS(Fnq)
        return 1 + IzXN + QWy

    def _lengthOfLIS(self, coordinates):
        def compare(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            else:
                if a[1] > b[1]:
                    return -1
                elif a[1] < b[1]:
                    return 1
                else:
                    return 0

        coordinates.sort(key=cmp_to_key(compare))

        def binarySearch(arr, val, low, high):
            if low >= high:
                return low
            midx = low + ((high - low) // 2)
            if arr[midx] < val:
                return binarySearch(arr, val, midx + 1, high)
            else:
                return binarySearch(arr, val, low, midx)

        agVz = []
        lenCo = len(coordinates)
        jFmB = 0
        while jFmB < lenCo:
            _, valY = coordinates[jFmB]
            if not agVz or valY > agVz[-1]:
                agVz.append(valY)
            else:
                posIx = binarySearch(agVz, valY, 0, len(agVz))
                agVz[posIx] = valY
            jFmB += 1
        return len(agVz)