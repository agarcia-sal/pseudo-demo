def main():
    # Step 2: Input Handling 
    number_of_elements = int(input())
    
    # Step 3: Initialization
    status_list = [True] * number_of_elements  # Initializing the list with True
    current_index = 0
    step_increment = 1

    # Step 4: Looping Process
    while step_increment <= 500000:
        if status_list[current_index]:  # Check the value at the current index
            status_list[current_index] = False  # Set it to False

        step_increment += 1  # Increment step
        current_index = (current_index + step_increment) % number_of_elements  # Wrap around using modulo

    # Step 5: Filtering Results
    true_values = [value for value in status_list if value]  # List of True values

    # Step 6: Output Handling
    if len(true_values) == 0:
        print("YES")
    else:
        print("NO")

# Step 1: Entry point of the program
if __name__ == "__main__":
    main()
