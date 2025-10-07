class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def multiplyFactorials(value: int) -> int:
            result = 1
            for idx in range(2, value + 1):
                result *= idx
            return result

        accumulator = 0
        encountered = set()
        factorialCache = []

        # Calculate upperLimit = 10 ^ ((n - 1) // 2)
        upperLimit = 10 ** ((n - 1) // 2)

        def buildFactorials(count: int) -> None:
            counter = 0
            while counter <= count:
                factorialCache.append(multiplyFactorials(counter))
                counter += 1

        buildFactorials(n)

        for candidate in range(upperLimit, upperLimit * 10):
            halfString = str(candidate)
            mirrorStart = n % 2
            suffix = halfString[::-1][mirrorStart:]
            fullString = halfString + suffix

            fullInt = int(fullString)
            if fullInt % k != 0:
                continue

            sortedForm = ''.join(sorted(fullString))
            if sortedForm in encountered:
                continue
            encountered.add(sortedForm)

            def frequencyMap(inputStr: str) -> dict:
                freq = {}
                for ch in inputStr:
                    freq[ch] = freq.get(ch, 0) + 1
                return freq

            counts = frequencyMap(sortedForm)
            totalCount = n

            if '0' in counts and counts['0'] > 0:
                productResult = (totalCount - counts['0']) * factorialCache[totalCount - 1]
            else:
                productResult = factorialCache[totalCount]

            for amount in counts.values():
                productResult //= factorialCache[amount]

            accumulator += productResult

        return accumulator