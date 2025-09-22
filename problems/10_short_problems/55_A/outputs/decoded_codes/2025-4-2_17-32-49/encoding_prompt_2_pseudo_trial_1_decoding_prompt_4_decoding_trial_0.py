def main():
    # Step 1: Receive the input value for the number of elements
    number_of_elements = int(input())
    
    # Step 2: Create a boolean list initialized to True
    boolean_list = [True] * number_of_elements
    
    # Step 3: Initialize index and step
    index = 0
    step = 1
    
    # Step 5: Process until step is less than or equal to 500,000
    while step <= 500000:
        # Check the current position in the booleanList
        if boolean_list[index]:
            # Change the current position in booleanList to False
            boolean_list[index] = False
            
        # Increment step
        step += 1
        
        # Update index, wrapping around using modulo
        index = (index + step) % number_of_elements
    
    # Step 6: Collecting all True elements
    true_elements = [i for i, value in enumerate(boolean_list) if value]
    
    # Step 7: Outputting results based on the length of trueElements
    if len(true_elements) == 0:
        print("YES")
    else:
        print("NO")

# Optional: This ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()
