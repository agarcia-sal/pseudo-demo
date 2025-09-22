# Start the program

# Step 2: Read an integer value 't' from the user
t = int(input())

# Step 3: Initialize a variable 'result' to zero
result = 0

# Step 4: For each integer 'i' from 1 to 't' (inclusive)
for i in range(1, t + 1):
    # Step 4a: Initialize a count variable 'count' to zero
    count = 0
    # Step 4b: Set 'currentNumber' to 'i'
    current_number = i
    
    # Step 5: For each integer 'j' from 2 to (i - 1)
    for j in range(2, current_number):
        # Step 5a: Check if 'currentNumber' is divisible by 'j'
        if current_number % j == 0:
            # Step 5b: If 'currentNumber' is divisible by 'j'
            count += 1  # Increment 'count' by 1
            
            # Step 5b.ii: While 'currentNumber' is divisible by 'j'
            while current_number % j == 0:
                # Step 5b.ii.1: Divide 'currentNumber' by 'j'
                current_number //= j  # Use integer division to remove the factor
    
    # Step 6: If 'count' is equal to 2
    if count == 2:
        result += 1  # Increment 'result' by 1

# Step 7: Output the value of 'result'
print(result)

# End the program
