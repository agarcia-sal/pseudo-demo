def count_prime_numbers():
    # Step 1: Get the input from the user
    t = int(input())
    
    # Step 2: Initialize the result variable to count prime numbers
    res = 0
    
    # Step 3: Loop through numbers from 1 to t (inclusive)
    for i in range(1, t + 1):
        cnt = 0  # To count distinct prime factors
        num = i  # Preserve the original number to factorize
        
        # Step 4: Check for factors from 2 to i - 1
        for j in range(2, i):
            if num % j == 0:  # j is a factor of num
                cnt += 1  # Count the distinct factor
                
                # Step 5: Remove this factor from num completely
                while num % j == 0:
                    num //= j
        
        # Step 6: If cnt equals 2, it means i has exactly two distinct prime factors
        if cnt == 2:
            res += 1  # Increment the count of prime numbers

    # Step 7: Output the total count of prime numbers
    print(res)

# Call the function to execute the program
count_prime_numbers()
