from typing import List

def hex_key(string_num: str) -> int:
    primeChars: List[str] = ['2', '3', '5', '7', 'B', 'D']

    def countPrimes(position: int, acc: int) -> int:
        if position >= len(string_num):
            return acc
        currentChar = string_num[position]
        if currentChar in primeChars:
            return countPrimes(position + 1, acc + 1)
        else:
            return countPrimes(position + 1, acc)

    return countPrimes(0, 0)