def main():
    # Step 1: Read a number from the user
    number_of_elements = int(input())

    # Step 2: Initialize an array of boolean values, all set to true
    boolean_array = [True] * number_of_elements

    # Step 3: Set initial counters
    position_index = 0
    step_counter = 1

    # Step 4: Loop until step_counter exceeds 500000
    while step_counter <= 500000:
        # Step 5: Check if the current position in the array is true
        if boolean_array[position_index]:
            # Step 6: Set the current position in the array to false
            boolean_array[position_index] = False
        
        # Step 7: Increment the step_counter
        step_counter += 1
        
        # Step 8: Update position_index based on the step_counter
        position_index = (position_index + step_counter) % number_of_elements
    
    # Step 9: Filter the boolean_array to find remaining true values
    remaining_true_values = [value for value in boolean_array if value]

    # Step 10: Check if there are any true values left in the filtered list
    if len(remaining_true_values) == 0:
        # Step 11: Print "YES" if there are no true values left
        print("YES")
    else:
        # Step 12: Print "NO" if there are still true values left
        print("NO")

if __name__ == "__main__":
    main()
