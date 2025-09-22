def main():
    # Step 1: Get input values
    first_input = input()
    second_input = input()

    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare the corresponding elements of the two lists
    for index in range(3):  # We assume there are at least 3 elements
        first_element = int(first_list[index])
        second_element = int(second_list[index])
        
        # If elements are different, increment the counter
        if first_element != second_element:
            difference_count += 1 

    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Execute the main function if the program is run as main
if __name__ == "__main__":
    main()
