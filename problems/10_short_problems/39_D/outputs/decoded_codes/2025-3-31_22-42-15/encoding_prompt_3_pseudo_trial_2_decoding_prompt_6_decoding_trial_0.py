def main():
    # Step 1: Collect input
    first_input = input()  # User inputs first sequence of numbers
    second_input = input()  # User inputs second sequence of numbers
    
    # Step 2: Split the input strings into separate components
    first_list = first_input.split()  # Splitting string into list of strings
    second_list = second_input.split()  # Splitting string into list of strings
    
    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter for differences
    
    # Step 4: Compare elements from both lists
    for index in range(3):  # Looping from index 0 to 2
        first_value = int(first_list[index])  # Convert the value to integer
        second_value = int(second_list[index])  # Convert the value to integer
        
        # Step 5: Check if the values are different
        if first_value != second_value:  # Comparing the values
            difference_count += 1  # Increment counter if they differ
    
    # Step 6: Determine the output based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Step 7: Execute the main function if this script is run
if __name__ == "__main__":
    main()
