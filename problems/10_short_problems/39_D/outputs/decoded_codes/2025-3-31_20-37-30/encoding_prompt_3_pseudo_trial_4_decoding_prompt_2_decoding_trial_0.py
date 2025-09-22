def main():
    # Take input for comparison
    string1 = input()
    string2 = input()

    # Split the input strings into lists of strings
    list1 = string1.split()
    list2 = string2.split()
    
    # Initialize a counter for differences
    differenceCounter = 0 

    # Compare corresponding elements in the lists
    for index in range(3):  # Assuming there are always 3 elements to compare
        # Convert the current elements to integers for comparison
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Check if the values are different
        if value1 != value2:
            differenceCounter += 1 

    # Determine if the number of differences is less than 3
    if differenceCounter < 3:
        print("YES")  # There are fewer than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Entry point of the program
if __name__ == "__main__":
    main()
