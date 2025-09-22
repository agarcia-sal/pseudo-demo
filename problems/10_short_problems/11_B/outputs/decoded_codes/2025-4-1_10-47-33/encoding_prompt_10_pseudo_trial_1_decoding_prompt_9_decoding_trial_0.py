# Start of the program

# Step 1: Get the absolute integer input
n = abs(int(input()))

# Step 2: Initialize the counter variable
i = 0

# Step 3: Begin an infinite loop to find the result
while True:  
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Using integer division
    
    # Calculate the difference between sum and input
    m = s - n
    
    # Step 4: Check if the sum equals n
    if s == n:
        print(i)
        break
        
    # Step 5: Check if the sum exceeds n
    elif s > n:
        # Step 6: Check if the difference is even
        if m % 2 == 0:
            print(i)
            break
    
    # Increment the counter for the next iteration
    i += 1

# End of the program
