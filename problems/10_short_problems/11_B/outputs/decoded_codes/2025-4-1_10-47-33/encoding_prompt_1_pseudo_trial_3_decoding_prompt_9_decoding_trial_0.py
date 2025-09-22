# Get absolute value of input
n = abs(int(input()))

# Initialize the counter variable
i = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first i natural numbers
    s = i * (i + 1) // 2
    
    # Calculate the difference
    m = s - n
    
    # Check if the sum is equal to n
    if s == n:
        print(i)
        break  # Exit the loop
    
    # Check if the sum is greater than n
    if s > n:
        # Check if the difference is an even number
        if m % 2 == 0:
            print(i)
            break  # Exit the loop
    
    # Increment i for the next number in the sequence
    i += 1
