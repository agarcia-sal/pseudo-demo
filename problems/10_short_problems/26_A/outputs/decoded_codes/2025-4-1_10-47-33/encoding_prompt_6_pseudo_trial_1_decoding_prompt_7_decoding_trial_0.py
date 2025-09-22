# Start the program

# Read an integer value 't' from the user
t = int(input())

# Initialize a variable 'result' to zero
result = 0

# For each integer 'i' from 1 to 't' (inclusive):
for i in range(1, t + 1):
    # Initialize a count variable 'count' to zero
    count = 0
    # Set 'currentNumber' to 'i'
    currentNumber = i
    
    # For each integer 'j' from 2 to (i - 1):
    for j in range(2, i):
        # Check if 'currentNumber' is divisible by 'j'
        if currentNumber % j == 0:
            # If 'currentNumber' is divisible by 'j':
            count += 1  # Increment 'count' by 1
            
            # While 'currentNumber' is divisible by 'j':
            while currentNumber % j == 0:
                # Divide 'currentNumber' by 'j' to remove the factor
                currentNumber //= j
    
    # If 'count' is equal to 2:
    if count == 2:
        # Increment 'result' by 1
        result += 1

# Output the value of 'result'
print(result)

# End the program
