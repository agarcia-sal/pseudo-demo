def main():
    # Step 1: Receive input
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists of substrings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 
    
    # Step 4: Loop through the indices of the lists
    for index in range(3):  # We assume the length of both lists is 3
        # Step 4a: Convert the string elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Step 4b: Check if the two values are different
        if first_value != second_value:
            difference_count += 1
        
    # Step 5: Evaluate the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program runs
if __name__ == "__main__":
    main()
