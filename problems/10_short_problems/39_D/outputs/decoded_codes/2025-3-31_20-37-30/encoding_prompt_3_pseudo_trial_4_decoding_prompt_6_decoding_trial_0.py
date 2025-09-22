def main():
    # Take input for comparison
    string1 = input()  # First string input from user
    string2 = input()  # Second string input from user

    # Split the input strings into lists of strings
    list1 = string1.split()  # Split string1 into list1
    list2 = string2.split()  # Split string2 into list2
    
    # Initialize a counter for differences
    difference_counter = 0 

    # Compare corresponding elements in the lists
    for index in range(3):  # Looping through the first three elements
        # Convert the current elements to integers for comparison
        value1 = int(list1[index])  # Convert to integer the current element from list1
        value2 = int(list2[index])  # Convert to integer the current element from list2
        
        # Check if the values are different
        if value1 != value2:
            difference_counter += 1  # Increment counter by 1 if values are different
    
    # Determine if the number of differences is less than 3
    if difference_counter < 3:
        print("YES")  # Output if fewer than 3 differences
    else:
        print("NO")   # Output if 3 or more differences

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function
