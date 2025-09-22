# Function to find the index of a triangular number that meets certain conditions
def find_triangular_index():
    # Step 1: Get user input and convert to absolute integer
    integer_value = abs(int(input()))
    
    # Step 2: Initialize a counter variable
    index = 0

    # Step 3: Create an infinite loop to find a solution
    while True:
        # Calculate the sum of the first 'index' natural numbers (triangular number)
        calculated_sum = (index * (index + 1)) // 2  # Using integer division
        
        # Calculate the difference between the calculated sum and the input value
        difference = calculated_sum - integer_value
        
        # Step 4: Check if the calculated sum matches the input value
        if calculated_sum == integer_value:
            # If they are equal, print the current index and exit the loop
            print(index)
            break
        
        # Step 5: Check if the calculated sum exceeds the input value
        elif calculated_sum > integer_value:
            # Check if the difference is even
            if difference % 2 == 0:
                # If the difference is even, print the current index and exit the loop
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Calling the function to execute
find_triangular_index()
