def main():
    # Read two input strings from the user
    FIRST_STRING = input()
    SECOND_STRING = input()
    
    # Split the input strings into lists of substrings
    LIST1 = FIRST_STRING.split()
    LIST2 = SECOND_STRING.split()
    
    # Initialize a counter for differences
    DIFFERENCE_COUNT = 0 
    
    # Compare the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the current elements to integers
        NUMBER1 = int(LIST1[index])
        NUMBER2 = int(LIST2[index])
        
        # Check if the numbers are different
        if NUMBER1 != NUMBER2:
            DIFFERENCE_COUNT += 1  # Increment DIFFERENCE_COUNT by 1
    
    # Determine if the number of differences is less than 3
    if DIFFERENCE_COUNT < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
