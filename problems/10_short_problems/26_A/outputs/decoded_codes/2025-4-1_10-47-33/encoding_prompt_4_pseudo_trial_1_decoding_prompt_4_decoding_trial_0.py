def count_numbers_with_two_prime_factors():
    # Step 1: Read the integer input 't'
    t = int(input())
    
    # Step 2: Initialize a variable 'result' to 0
    result = 0
    
    # Step 3: Loop through each integer 'i' from 1 to 't' (inclusive)
    for i in range(1, t + 1):
        # Initialize a variable 'count' to 0
        count = 0
        number = i
        
        # Step 4: Check for prime factors from 2 to 'i - 1'
        for j in range(2, i):
            # If 'number' is divisible by 'j'
            if number % j == 0:
                count += 1  # Increment 'count' by 1
                # Step 4a: While 'number' is divisible by 'j'
                while number % j == 0:
                    number //= j  # Divide 'number' by 'j'
        
        # Step 5: If 'count' is equal to 2
        if count == 2:
            result += 1  # Increment 'result' by 1
    
    # Step 6: Output 'result'
    print(result)

# Run the function
count_numbers_with_two_prime_factors()
