def main():
    # Step 1: Gather input
    first_input = input()
    second_input = input()

    # Step 2: Split input into individual components
    first_input_components = first_input.split()
    second_input_components = second_input.split()
    
    # Step 3: Initialize a counter for differences
    difference_counter = 0
    
    # Step 4: Compare corresponding components from both inputs
    for index in range(3):  # We assume there are at least 3 components based on the pseudocode
        first_value = int(first_input_components[index])
        second_value = int(second_input_components[index])
        
        # If the values are not equal, increment the difference counter
        if first_value != second_value:
            difference_counter += 1
            
    # Step 5: Determine and output the result based on the number of differences
    result = "YES" if difference_counter < 3 else "NO"
    print(result)

if __name__ == "__main__":
    main()


    1 2 3
    1 2 3
    

    1 2 3
    4 2 5
    

    10 20 30
    10 21 30
    