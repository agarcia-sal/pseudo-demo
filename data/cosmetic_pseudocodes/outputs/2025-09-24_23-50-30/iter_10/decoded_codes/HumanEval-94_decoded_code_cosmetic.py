from typing import List


def skjkasdkd(array_of_nums: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        check = 2
        while check * check <= num:
            if num % check == 0:
                return False
            check += 1
        return True

    highest_prime = 0
    for idx in range(len(array_of_nums)):
        num = array_of_nums[idx]
        if num > highest_prime and isPrime(num):
            highest_prime = num

    total = 0
    digits = str(highest_prime)
    pos = 0
    while pos < len(digits):
        total += int(digits[pos])
        pos += 1

    return total