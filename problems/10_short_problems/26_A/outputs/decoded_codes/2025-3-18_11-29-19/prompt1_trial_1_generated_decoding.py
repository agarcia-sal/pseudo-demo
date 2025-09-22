# Start the program

# Read an integer value t from user input
t = int(input())

# Initialize a variable result to 0
result = 0

# Loop through each integer i from 1 to t (inclusive)
for i in range(1, t + 1):
    # Initialize a counter count to 0
    count = 0
    # Set a temporary variable number equal to i
    number = i

    # Loop through each integer j from 2 to i-1
    for j in range(2, i):
        # Check if number is divisible by j
        if number % j == 0:
            # Increment the count of prime factors by 1
            count += 1
            
            # While number is still divisible by j
            while number % j == 0:
                # Divide number by j
                number //= j

    # Check if count is equal to 2
    if count == 2:
        # Increment result by 1
        result += 1

# Output the value of result
print(result)

# End of program
