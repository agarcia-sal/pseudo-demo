class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD_VALUE = 10_000_000_007

        def modulus(x: int, y: int) -> int:
            return x % y

        def initializeArray(size: int, outArr: list[int]) -> None:
            for index in range(size):
                outArr[index] = 1

        def updateArray(arr: list[int], size: int) -> None:
            position = 1
            while position < size:
                arr[position] = modulus(arr[position] + arr[position - 1], MOD_VALUE)
                position += 1

        buffer = [0] * n
        initializeArray(n, buffer)

        counterOuter = 0
        while counterOuter < k:
            updateArray(buffer, n)
            counterOuter += 1

        return buffer[n - 1]