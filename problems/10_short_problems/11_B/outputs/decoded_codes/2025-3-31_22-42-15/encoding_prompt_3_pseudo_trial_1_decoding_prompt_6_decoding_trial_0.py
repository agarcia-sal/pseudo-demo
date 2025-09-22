# Begin the program

# Step 1: Get user input and convert it to absolute value
user_input = int(input())  #Read input from user and convert to integer
absolute_value = abs(user_input)  #Get the absolute value of the input

# Step 2: Initialize a counter for triangular numbers
index = 0  # Starting index for triangular number calculation

# Step 3: Infinite loop to calculate triangular numbers
while True:  
    # Calculate the triangular number for the current index
    triangular_number = (index * (index + 1)) // 2  # Using integer division to calculate triangular number
    
    # Calculate the difference between the triangular number and the user input
    difference = triangular_number - absolute_value
    
    # Check if the triangular number equals the absolute input
    if triangular_number == absolute_value:
        print(index)  # Print the current index
        break  # Exit the loop
    
    # Check if the triangular number exceeds the absolute input
    elif triangular_number > absolute_value:
        # If the difference is even
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the current index
            break  # Exit the loop
    
    # Increment the index to check the next triangular number
    index += 1  # Move to the next index
