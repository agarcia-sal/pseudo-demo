class Solution:
    def maximumEnergy(self, energy, k):
        def lengthOf(lst):
            # Simply returns the length of a list, straightforward in Python
            return lengthOfHelper(lst, 0)

        def lengthOfHelper(lst, acc):
            if acc == 0:
                return lengthRecursive(lst, acc)
            else:
                return acc

        def lengthRecursive(lst, acc):
            if acc >= 0:
                temp = acc
                if temp >= 0:
                    return lengthIterate(lst, temp, 1)
                else:
                    return 0
            else:
                return 0

        def lengthIterate(lst, current, step):
            # The pseudocode seems to implement length, but in Python we simply use len()
            # However, to keep structure, we will implement the termination when step exceeds current
            # This obfuscated code essentially hints at obtaining the length by iteration
            if current >= step:
                return lengthIterate(lst, current, step + 1)
            else:
                return step

        def zeroList(size):
            # Create a list of zeros of given size
            return [0] * size

        def emptyList():
            return []

        def appendToList(lst, val):
            lst.append(val)

        def lastIndex(lst):
            return lengthOf(lst) - 1

        n = lengthOf(energy)
        dp = zeroList(n)
        last_idx = lastIndex(dp)
        dp[last_idx] = energy[last_idx]
        max_energy = dp[last_idx]

        def createDeque(initial):
            d = emptyList()
            appendToList(d, initial)
            return d

        def dequeIsEmpty(dq):
            return lengthOf(dq) == 0

        def dequeFront(dq):
            return dq[0]

        def dequeBack(dq):
            return dq[lengthOf(dq) - 1]

        def dequePopFront(dq):
            # Remove front element by returning a new list without first element
            # To keep immutability as in pseudocode
            tempDQ = emptyList()
            idx = 1
            while idx < lengthOf(dq):
                appendToList(tempDQ, dq[idx])
                idx += 1
            return tempDQ

        def dequePopBack(dq):
            # Remove back element by returning a new list without last element
            tempDQ = emptyList()
            i = 0
            while i < lengthOf(dq) - 1:
                appendToList(tempDQ, dq[i])
                i += 1
            return tempDQ

        def dequePushBack(dq, val):
            appendToList(dq, val)

        reference = createDeque(n - 1)

        def loop_i(i, n, dp, energy, reference, max_energy):
            if i < 0:
                return max_energy
            else:
                while lengthOf(reference) > 0 and (dequeFront(reference) - i) >= k:
                    reference = dequePopFront(reference)

                dp[i] = energy[i] + dp[dequeFront(reference)]

                if max_energy < dp[i]:
                    max_energy = dp[i]

                while (not dequeIsEmpty(reference)) and dp[i] >= dp[dequeBack(reference)]:
                    reference = dequePopBack(reference)

                dequePushBack(reference, i)
                return loop_i(i - 1, n, dp, energy, reference, max_energy)

        return loop_i(n - 2, n, dp, energy, reference, max_energy)