def main():
    # Read input values from user
    first_string = input()  # User inputs the first string
    second_string = input()  # User inputs the second string
    
    # Split the input strings into lists of items
    first_list = first_string.split()  # Split first string into a list
    second_list = second_string.split()  # Split second string into a list
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from both lists to integers
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Compare the two values
        if first_value != second_value:  # Check if values are not equal
            # If they are different, increment the difference counter
            difference_count += 1
    
    # Check the count of differences
    if difference_count < 3:  # If there are fewer than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Otherwise, output "NO"

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
