# Function to find the smallest non-negative integer 'i'
# such that the sum of the first 'i' integers is >= n
def find_smallest_integer():
    # Step 1: Accept user input and convert it to a non-negative integer
    number = abs(int(input()))  # Get absolute value of the user input
    
    # Step 2: Initialize a counter for the number of integers summed
    index = 0
    
    # Step 3: Start an infinite loop to compute the sum of integers
    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_integers = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the input number
        difference = sum_of_integers - number
        
        # Step 4: Check if the sum equals the input number
        if sum_of_integers == number:
            print(index)  # Output the current index
            break  # Exit the loop
            
        # Step 5: Check if the sum exceeds the input number
        elif sum_of_integers > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop
                
        # Increment the index for the next iteration
        index += 1

# Call the function to execute
find_smallest_integer()
