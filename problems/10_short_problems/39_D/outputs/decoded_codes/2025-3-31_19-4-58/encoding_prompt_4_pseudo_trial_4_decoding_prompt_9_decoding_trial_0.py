def main():
    # Read input values
    t1 = input()  # First string input
    t2 = input()  # Second string input

    # Split the input strings into lists
    tt1 = t1.split()  # Convert first string to a list of substrings
    tt2 = t2.split()  # Convert second string to a list of substrings
    
    # Initialize the result counter
    difference_count = 0 

    # Compare the first three elements of both lists
    for index in range(3):
        a = int(tt1[index])  # Convert the first list element to an integer
        b = int(tt2[index])  # Convert the second list element to an integer
        if a != b:  # Check if the two integers are not equal
            difference_count += 1  # Increment the difference counter

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO if differences are 3 or more

# Execute the main function when the script runs
main()  
