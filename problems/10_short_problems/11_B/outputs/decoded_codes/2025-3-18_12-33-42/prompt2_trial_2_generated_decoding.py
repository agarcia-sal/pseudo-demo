# Step 1: Start
# Step 2: Prompt the user for input and store it as an integer
n = abs(int(input()))  # Get the absolute value of the input integer

# Step 3: Initialize a variable 'i' to 0
i = 0

# Step 4: Begin an infinite loop
while True:
    # Step 4a: Calculate the sum 's' of the first 'i' natural numbers
    s = (i * (i + 1)) / 2
    
    # Step 4b: Calculate the difference 'm' between 's' and 'n'
    m = s - n

    # Step 4c: Check if 's' is equal to 'n'
    if s == n:
        print(i)  # If true, print the value of 'i' and exit the loop
        break  # Exit the loop

    # Step 4d: Check if 's' is greater than 'n'
    if s > n:
        # Check if 'm' is even
        if m % 2 == 0:
            print(i)  # If true, print the value of 'i' and exit the loop
            break  # Exit the loop
    
    # Step 4e: Increment 'i' by 1
    i += 1

# Step 5: End
