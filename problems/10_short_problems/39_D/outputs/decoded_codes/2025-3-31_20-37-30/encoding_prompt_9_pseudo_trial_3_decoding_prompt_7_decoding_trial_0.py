def main():
    # Step 1: Receive input from the user
    first_input = input()  # Reading the first input
    second_input = input()  # Reading the second input
    
    # Step 2: Split the input strings into lists of substrings
    first_list = first_input.split()  # Splitting the first input
    second_list = second_input.split()  # Splitting the second input
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 
    
    # Step 4: Loop through the indices of the lists
    for index in range(3):  # Looping from 0 to 2 (inclusive)
        # Step 4a: Convert the string elements to integers
        first_value = int(first_list[index])  # Convert first list element to integer
        second_value = int(second_list[index])  # Convert second list element to integer
        
        # Step 4b: Check if the two values are different
        if first_value != second_value:  # If they are not equal
            difference_count += 1  # Increment the difference count
    
    # Step 5: Evaluate the count of differences
    if difference_count < 3:  # If fewer than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Execute the main function when the program runs
if __name__ == "__main__":
    main()  # Calling the main function
