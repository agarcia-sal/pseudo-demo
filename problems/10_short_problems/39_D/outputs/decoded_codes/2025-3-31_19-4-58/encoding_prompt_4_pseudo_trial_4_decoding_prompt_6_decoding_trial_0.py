def main():
    # Read input values
    first_string = input()  # Get user input for the first string
    second_string = input()  # Get user input for the second string

    # Split the input strings into lists
    list_first_string = first_string.split()  # Split first string into a list
    list_second_string = second_string.split()  # Split second string into a list
    
    # Initialize the result counter
    difference_count = 0 

    # Compare the first three elements of both lists
    for index in range(3):  # Loop through indices 0 to 2
        a = int(list_first_string[index])  # Convert the element to integer
        b = int(list_second_string[index])  # Convert the element to integer
        if a != b:  # Check if the two integers are not equal
            difference_count += 1  # Increment difference count

    # Check if the number of differences is less than 3
    if difference_count < 3:  
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO otherwise

# Execute the main function when the script runs
if __name__ == "__main__":
    main()
