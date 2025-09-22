def main():
    # Take input for comparison
    string1 = input()  # Input first string from user
    string2 = input()  # Input second string from user

    # Split the input strings into lists of strings
    list1 = string1.split()  # Split first string into a list
    list2 = string2.split()  # Split second string into a list
    
    # Initialize a counter for differences
    difference_counter = 0 

    # Compare corresponding elements in the lists
    for index in range(3):  # Loop through the first three elements
        # Convert the current elements to integers for comparison
        value1 = int(list1[index])  # Convert element from list1 to integer
        value2 = int(list2[index])  # Convert element from list2 to integer
        
        # Check if the values are different
        if value1 != value2:  # If values are not equal
            difference_counter += 1  # Increment the difference counter
    
    # Determine if the number of differences is less than 3
    if difference_counter < 3:  # If differences are fewer than 3
        print("YES")  # Output "YES"
    else:
        print("NO")   # Output "NO"

# Entry point of the program
if __name__ == "__main__":  # Check if this script is run as the main program
    main()  # Call the main function
