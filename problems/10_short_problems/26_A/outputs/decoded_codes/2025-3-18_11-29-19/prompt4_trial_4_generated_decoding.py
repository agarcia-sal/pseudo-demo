def count_numbers_with_two_prime_factors():
    # Step 1: Read an integer value 't' from user input
    t = int(input())
    
    # Step 2: Initialize a variable 'result' to 0
    result = 0

    # Step 3: For each integer 'i' from 1 to 't' (inclusive)
    for i in range(1, t + 1):
        count = 0  # Step 3a: Initialize a variable 'count' to 0
        number = i  # Step 3b: Set 'number' to 'i'
        
        # Step 3c: For each integer 'j' from 2 to 'i-1'
        for j in range(2, i):
            if number % j == 0:  # Step 3ci: Check if 'number' is divisible by 'j'
                count += 1  # Increment 'count' by 1
                
                # Step 3cii: While 'number' is divisible by 'j'
                while number % j == 0:
                    number //= j  # Use floor division to divide 'number' by 'j'
        
        # Step 3d: Check if 'count' is equal to 2
        if count == 2:
            result += 1  # Increment 'result' by 1

    # Step 4: Output 'result'
    print(result)

# Run the function
count_numbers_with_two_prime_factors()
