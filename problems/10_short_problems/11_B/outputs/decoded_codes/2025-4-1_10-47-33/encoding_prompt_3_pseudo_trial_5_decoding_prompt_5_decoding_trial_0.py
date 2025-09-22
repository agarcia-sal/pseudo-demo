# Function to find the index of the first natural number 
# where the sum matches the absolute user input or 
# the difference is even
def find_matching_index():
    # Step 1: Read an integer input from the user
    user_input = abs(int(input()))  # Absolute value of the user input
    index = 0  # Initialize index

    # Step 2: Infinite loop to find the required index
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_natural = (index * (index + 1)) // 2
        
        # Calculate the difference from the user input
        difference = sum_natural - user_input
        
        # Step 3: Check if we found the desired sum
        if sum_natural == user_input:
            print(index)  # Output the index
            break  # Exit the loop
        
        # Step 4: If sum is greater than user input
        elif sum_natural > user_input:
            # Step 5: Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break  # Exit the loop
        
        # Step 6: Increment index for the next iteration
        index += 1  # Move to the next natural number

# Uncomment the following line to run the function
# find_matching_index()
