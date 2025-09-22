# Start

# Input
n = abs(int(input()))

# Initialize
i = 0

# Loop
while True:
    # Calculate the sum s of the first i natural numbers
    s = i * (i + 1) // 2
    # Compute m
    m = s - n
    
    # Conditional Checks
    if s == n:
        print(i)
        break
    if s > n:
        if m % 2 == 0:  # Check if m is even
            print(i)
            break
    
    # Increment
    i += 1

# End
