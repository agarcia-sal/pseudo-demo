def count_numbers_with_two_prime_factors():
    # Step 1: Declare and initialize variables
    t = 0
    res = 0

    # Step 2: Input number of test cases
    print("Enter the number of cases:")
    t = int(input())

    # Step 3: Loop through each number from 1 to t
    for i in range(1, t + 1):
        cnt = 0
        num = i
        
        # Step 4: Check for factors of the current number
        for j in range(2, i):
            if num % j == 0:
                cnt += 1
                
                # Step 5: Divide num by j as long as it's divisible
                while num % j == 0:
                    num //= j
        
        # Step 6: Check if the number has exactly two prime factors
        if cnt == 2:
            res += 1

    # Step 7: Output the result
    print(res)

# Call the function to execute the logic
count_numbers_with_two_prime_factors()
