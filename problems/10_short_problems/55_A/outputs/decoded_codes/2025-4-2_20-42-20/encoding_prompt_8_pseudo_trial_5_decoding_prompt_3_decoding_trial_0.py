def main():
    # Step 1: Read the number of elements from user input
    number_of_elements = int(input())
    
    # Step 2: Initialize the boolean list and variables
    boolean_list = [True] * number_of_elements
    pointer = 0
    index = 1

    # Step 3: Loop while index is less than or equal to 500000
    while index <= 500000:
        if boolean_list[pointer]:  # If current element is True
            boolean_list[pointer] = False  # Set current element to False
        
        index += 1  # Increment index
        pointer = (pointer + index) % number_of_elements  # Update pointer

    # Step 4: Filter active elements that are still True
    active_elements = [val for val in boolean_list if val]

    # Step 5: Check result and print accordingly
    if len(active_elements) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
