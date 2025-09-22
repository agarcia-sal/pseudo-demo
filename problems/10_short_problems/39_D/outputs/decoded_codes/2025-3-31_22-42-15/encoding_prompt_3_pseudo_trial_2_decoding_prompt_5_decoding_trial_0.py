def main():
    # Step 1: Collect input from the user
    first_input = input()  # Input for the first sequence of numbers
    second_input = input()  # Input for the second sequence of numbers

    # Step 2: Split the input strings into separate components
    first_list = first_input.split()  # Split the first input into a list of strings
    second_list = second_input.split()  # Split the second input into a list of strings

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare elements from both lists
    for index in range(3):  # Iterate through the first three elements
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Step 5: Check if the values are different
        if first_value != second_value:  # If they are not equal
            difference_count += 1  # Increment the difference count

    # Step 6: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function if this script is run
if __name__ == "__main__":
    main()
