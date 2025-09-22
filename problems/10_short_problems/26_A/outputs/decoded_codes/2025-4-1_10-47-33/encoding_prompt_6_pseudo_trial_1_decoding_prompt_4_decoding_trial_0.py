def main():
    # Step 2: Read an integer value 't' from the user
    t = int(input())
    
    # Step 3: Initialize a variable 'result' to zero
    result = 0

    # Step 4: For each integer 'i' from 1 to 't' (inclusive):
    for i in range(1, t + 1):
        # Step 4a: Initialize a count variable 'count' to zero
        count = 0
        current_number = i
        
        # Step 5: For each integer 'j' from 2 to (i - 1):
        for j in range(2, i):
            # Step 5a: Check if 'currentNumber' is divisible by 'j'
            if current_number % j == 0:
                # Step 5b: If 'currentNumber' is divisible by 'j'
                count += 1  # Increment the count of unique prime factors
                
                # Step 6b: While 'currentNumber' is divisible by 'j'
                while current_number % j == 0:
                    current_number //= j  # Remove the factor

        # Step 6: If 'count' is equal to 2
        if count == 2:
            result += 1  # Increment the result

    # Step 7: Output the value of 'result'
    print(result)

# Step 1: Start the program
if __name__ == "__main__":
    main()
