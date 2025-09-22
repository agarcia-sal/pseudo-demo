# Start of the program
# Importing necessary module for absolute value calculation
abs = abs  

# Step 2: Declare Variables
n = abs(int(input()))  # Get absolute value of integer input
i = 0  # Initialize i

# Step 3: Begin Infinite Loop
while True:
    # Calculate triangular number s as the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Use integer division to ensure s is an integer

    # Set variable m to s - n
    m = s - n  
    
    # Step 4: Check Conditions
    if s == n:
        print(i)  # Display the value of i
        break  # Exit the loop
    elif s > n:
        if m % 2 == 0:  # Check if m is an even number
            print(i)  # Display the value of i
            break  # Exit the loop
    
    # Step 5: Increment i by 1
    i += 1  # Increment i for the next iteration
# End of the program
