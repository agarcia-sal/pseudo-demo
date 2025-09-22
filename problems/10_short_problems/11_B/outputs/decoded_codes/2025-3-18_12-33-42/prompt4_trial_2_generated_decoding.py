# Read input value and calculate its absolute integer representation
n = abs(int(input()))

# Initialize the counter
i = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Using integer division as we are looking for an integer sum
    
    # Calculate the difference between sum and input
    m = s - n
    
    # Check if the calculated sum equals the input
    if s == n:
        print(i)  # Output the current index i
        break  # Exit the loop
    
    # Check if sum exceeds the input
    elif s > n:
        # Check if the difference is even
        if m % 2 == 0:
            print(i)  # Output the current index i
            break  # Exit the loop
            
    # Increment the counter
    i += 1
