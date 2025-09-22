def main():
    # Step 2: Input Number of Test Cases
    t = int(input())
    
    # Step 3: Initialize Result Counter
    res = 0  # This will hold the count of numbers with exactly two distinct prime factors

    # Step 4: Loop Through Each Number from 1 to t
    for i in range(1, t + 1):
        cnt = 0  # Counter for distinct prime factors
        num = i  # Set variable num to i (current number to factorize)

        # Step 5: Loop to Find Factors
        for j in range(2, i):
            # Check if j is a factor of num
            if num % j == 0:
                cnt += 1  # Found a new prime factor
                
                # While num is divisible by j, divide num by j
                while num % j == 0:
                    num //= j  # Remove factor j from num

        # Step 6: Check for Prime Condition
        if cnt == 2:  # Verify that i has exactly two distinct prime factors
            res += 1  # Count this number as valid

    # Step 7: Output Result
    print(res)  # Total count of numbers with exactly two distinct prime factors

# Start the program
if __name__ == "__main__":
    main()
