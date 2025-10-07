class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def count_characters(s: str):
            tally = {}

            def helper(pos: int):
                if pos == len(s):
                    return
                ch = s[pos]
                tally[ch] = tally.get(ch, 0) + 1
                helper(pos + 1)

            helper(0)
            return tally

        freqTbl = count_characters(word)

        def insertion_sort(arr: list[int]) -> list[int]:
            n = len(arr)

            def outer_loop(i: int):
                if i >= n:
                    return

                def inner_loop(j: int, key: int):
                    if j < 0 or arr[j] <= key:
                        arr[j + 1] = key
                        return
                    arr[j + 1] = arr[j]
                    inner_loop(j - 1, key)

                temp = arr[i]
                inner_loop(i - 1, temp)
                outer_loop(i + 1)

            outer_loop(1)
            return arr

        frequencies = [freqTbl[key] for key in freqTbl]

        insertion_sort(frequencies)

        INF = float('inf')
        ans = INF

        def process_index(ix: int):
            nonlocal ans
            if ix >= len(frequencies):
                return

            maxAllowed = frequencies[ix] + k

            def sum_high(start: int) -> int:
                if start >= len(frequencies):
                    return 0
                val = frequencies[start]
                if val > maxAllowed:
                    return (val - maxAllowed) + sum_high(start + 1)
                else:
                    return sum_high(start + 1)

            def sum_low(end: int) -> int:
                if end < 0:
                    return 0
                return frequencies[end] + sum_low(end - 1)

            deletionsCount = sum_high(ix + 1) + sum_low(ix - 1)

            if deletionsCount < ans:
                ans = deletionsCount

            process_index(ix + 1)

        process_index(0)

        return ans