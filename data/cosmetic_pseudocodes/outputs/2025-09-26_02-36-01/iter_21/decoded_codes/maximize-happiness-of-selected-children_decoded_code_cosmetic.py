class Solution:
    def maximumHappinessSum(self, happiness, k):
        def sortDescending(arr):
            def swapElements(x, y):
                arr[x], arr[y] = arr[y], arr[x]

            length = 0
            while length + 1 <= len(arr):
                length += 1

            index1 = length - 1
            while index1 >= 0:
                index2 = 0
                while index2 < index1:
                    if not (arr[index2] >= arr[index2 + 1]):
                        swapElements(index2, index2 + 1)
                    index2 += 1
                index1 -= 1

        totalSum = 0
        dec = 0
        pos = 0

        sortDescending(happiness)

        while True:
            if pos >= k:
                break

            current_diff = happiness[pos] - dec

            if not (current_diff >= 0):
                temp_var = 0
            else:
                temp_var = current_diff

            totalSum += temp_var
            dec += 1
            pos += 1

        return totalSum