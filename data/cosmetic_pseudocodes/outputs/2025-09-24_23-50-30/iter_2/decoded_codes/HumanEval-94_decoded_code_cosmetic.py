from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value <= 1:
            return False
        divisor = int(integer_value**0.5) + 1
        return all(integer_value % k != 0 for k in range(2, divisor))

    def findMaxPrimeRec(i: int, current_max: int) -> int:
        if i == len(list_of_integers):
            return current_max
        current_num = list_of_integers[i]
        if not (current_num <= current_max or not isPrime(current_num)):
            current_max = current_num
        return findMaxPrimeRec(i + 1, current_max)

    max_prime_value = findMaxPrimeRec(0, 0)

    def digitSum(n: int, acc: int) -> int:
        if n == 0:
            return acc
        return digitSum(n // 10, acc + (n % 10))

    return digitSum(max_prime_value, 0)