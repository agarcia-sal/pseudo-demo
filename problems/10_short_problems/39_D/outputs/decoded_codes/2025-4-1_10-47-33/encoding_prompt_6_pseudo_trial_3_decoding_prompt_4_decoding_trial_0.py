def do_main():
    # Step 1: Read input values.
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists of words.
    first_input_list = first_input.split()
    second_input_list = second_input.split()
    
    # Step 3: Initialize a counter for differences.
    difference_count = 0
    
    # Step 4: Compare corresponding elements in both lists.
    for index in range(3):
        # Convert string elements to integers for comparison.
        value_from_first_list = int(first_input_list[index])
        value_from_second_list = int(second_input_list[index])
        
        # Check if the values are different.
        if value_from_first_list != value_from_second_list:
            difference_count += 1
    
    # Step 5: Determine result based on the number of differences.
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block.
if __name__ == "__main__":
    do_main()


    1 2 3
    1 2 3
    

    1 2 3
    4 2 3
    

    1 2 3
    4 5 6
    

    1 1 1
    1 2 2
    