# Step 1: Read the input value for t (an integer representing the upper limit).
upper_limit = int(input())

# Step 2: Initialize a variable named prime_count to 0 (this will store the number of semiprimes).
semiprime_count = 0

# Step 3: For each number i from 1 to upper_limit (inclusive):
for number in range(1, upper_limit + 1):
    # a. Initialize a variable named divisor_count to 0 (this will count distinct prime factors of number).
    distinct_prime_count = 0
    # b. Set a variable current_number to number (to manipulate during factorization).
    current_number = number

    # c. For each number j from 2 to (number - 1):
    for divisor in range(2, number):
        # i. Check if j is a divisor of current_number (if current_number modulo j equals 0):
        if current_number % divisor == 0:
            # If true, increment divisor_count by 1 (indicating a distinct prime factor).
            distinct_prime_count += 1
            
            # While current_number is divisible by j (while current_number modulo j equals 0):
            while current_number % divisor == 0:
                # - Divide current_number by j (reduce current_number by removing prime factor j).
                current_number //= divisor

    # d. After the inner loop, check if divisor_count equals 2:
    if distinct_prime_count == 2: 
        # If true, increment prime_count by 1 (this number number is a semiprime).
        semiprime_count += 1

# Step 4: After all iterations, print the value of semiprime_count.
print(semiprime_count)
