# Start of the program

# Step 1: Get input from the user and take the absolute value
number = abs(int(input()))  # Taking absolute value of user's input number 

# Step 2: Initialize a variable to keep track of the current integer
currentInteger = 0  # Start with the smallest non-negative integer

# Step 3: Enter an infinite loop to search for the desired integer
while True:
    # Calculate the sum of the first 'currentInteger' integers
    sum = (currentInteger * (currentInteger + 1)) // 2  # Using integer division to get the sum
    
    # Calculate the difference between 'sum' and 'number'
    difference = sum - number  # Finding how much more the sum is than the input number
    
    # Step 4: Check if the sum equals the user's number
    if sum == number:
        print(currentInteger)  # Output the current integer
        break  # Exit the loop
    
    # Step 5: Check if sum is greater than the user's number
    elif sum > number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(currentInteger)  # Output the current integer
            break  # Exit the loop
    
    # Step 6: Increment the current integer for the next iteration
    currentInteger += 1  # Move to the next integer
