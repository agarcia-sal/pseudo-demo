def do_main():
    # Declare variables for input strings
    input_string1 = input()  # First line of input
    input_string2 = input()  # Second line of input
    
    # Split the input strings into lists of substrings
    list1 = input_string1.split()  # Split first input by spaces
    list2 = input_string2.split()  # Split second input by spaces
    
    # Initialize a variable to count differences
    differences_count = 0
    
    # Iterate over the first three elements of both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert string elements to integers
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Check if the values are different
        if value1 != value2:
            differences_count += 1  # Increment count if they differ
    
    # Determine if the number of differences is less than three
    if differences_count < 3:
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")   # Print "NO" otherwise

# Main execution block
do_main()
