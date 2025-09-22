def main():
    # Accept user input for the number of boolean values
    number_of_values = int(input())
    
    # Create a list of boolean values initialized to True
    boolean_list = [True] * number_of_values
    
    # Initialize control variables
    index = 0
    step = 1
    
    # Begin loop that operates until step exceeds 500,000
    while step <= 500_000:
        # If the current position in the list is still marked as True
        if boolean_list[index]:
            # Mark the current position as False (used)
            boolean_list[index] = False
            
        # Increment step to move to the next position
        step += 1
        
        # Calculate the next index to check using the current step and wrap around using modulo
        index = (index + step) % number_of_values
    
    # Check if there are no True values left in the boolean list
    if all(value is False for value in boolean_list):
        print("YES")
    else:
        print("NO")

# Run the main function
main()
