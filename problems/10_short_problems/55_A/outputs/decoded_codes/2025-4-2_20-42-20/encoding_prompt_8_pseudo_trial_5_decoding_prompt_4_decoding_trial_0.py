def main():
    # Step 1: Read the number of elements from user input
    number_of_elements = int(input())
    
    # Step 2: Initialize boolean list and other variables
    boolean_list = [True] * number_of_elements
    pointer = 0
    index = 1

    # Step 3: Loop to modify boolean_list based on specified conditions
    while index <= 500000:
        if boolean_list[pointer]:  # Check if the current pointer is True
            boolean_list[pointer] = False  # Set it to False
        
        index += 1  # Increment index
        pointer = (pointer + index) % number_of_elements  # Update pointer position

    # Step 4: Filter active elements
    active_elements = [element for element in boolean_list if element]

    # Step 5: Check results and print "YES" or "NO"
    if len(active_elements) == 0:
        print("YES")
    else:
        print("NO")

# Running the main function
if __name__ == "__main__":
    main()
