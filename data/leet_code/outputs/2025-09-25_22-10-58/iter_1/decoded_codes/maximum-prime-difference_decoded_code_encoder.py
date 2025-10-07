class Solution:
    def maximumPrimeDifference(self, nums):
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        first_prime_index = -1
        last_prime_index = -1
        for i, num in enumerate(nums):
            if num in primes:
                if first_prime_index == -1:
                    first_prime_index = i
                last_prime_index = i
        return last_prime_index - first_prime_index