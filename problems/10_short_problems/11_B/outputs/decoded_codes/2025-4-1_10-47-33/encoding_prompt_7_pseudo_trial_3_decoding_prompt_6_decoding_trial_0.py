# Function to find the smallest non-negative integer whose triangular number
# satisfies specific conditions with the given input value
def find_integer_with_triangle_number():
    # Step 1: Read the input value and calculate its absolute value
    input_value = int(input())  # Assuming the input is provided as an integer
    absolute_value = abs(input_value)
    
    # Step 2: Initialize the counter variable
    counter = 0
    
    # Step 3: Begin an infinite loop to calculate triangular numbers
    while True:
        # Calculate the current triangular number using the formula
        triangular_number = (counter * (counter + 1)) // 2
        
        # Calculate the difference between the triangular number and the absolute value
        difference = triangular_number - absolute_value
        
        # Step 4: Check if the triangular number equals the absolute value
        if triangular_number == absolute_value:
            print(counter)  # Found a match, output the counter
            break  # Exit the loop
        
        # Step 5: Check if the triangular number is greater than the absolute value
        elif triangular_number > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)  # Found a match, output the counter
                break  # Exit the loop
        
        # Increment the counter for the next triangular number
        counter += 1

# Call the function to execute it
find_integer_with_triangle_number()
