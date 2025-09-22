# Function to count semi-prime numbers up to a given number `t`
def count_semi_primes():
    # Step 2: Read an integer value `t` (representing the upper limit)
    t = int(input())
    # Step 3: Initialize `result` to 0 to keep track of the count of semi-prime numbers
    result = 0

    # Step 4: For each integer `i` from 1 to `t` (inclusive)
    for i in range(1, t + 1):
        # Step 4.1: Initialize `countDivisors` to 0 to count distinct prime factors of `i`
        countDivisors = 0
        # Step 4.2: Set `currentNumber` to `i`
        currentNumber = i

        # Step 4.3: For each integer `j` from 2 to (i-1)
        for j in range(2, i):
            # Step 4.3.1: If `currentNumber` is divisible by `j`
            if currentNumber % j == 0:
                # Step 4.3.1.1: Increment `countDivisors` by 1 (found a new prime factor)
                countDivisors += 1
                # Step 4.3.1.2: While `currentNumber` is divisible by `j`
                while currentNumber % j == 0:
                    # Step 4.3.1.2.1: Divide `currentNumber` by `j`
                    currentNumber //= j
        
        # Step 4.4: If `countDivisors` is equal to 2
        if countDivisors == 2:
            # Step 4.4.1: Increment `result` by 1 (i is a semi-prime number)
            result += 1

    # Step 5: Output the total count of semi-prime numbers found
    print(result)

# Calling the function to execute the semi-prime counting
count_semi_primes()
