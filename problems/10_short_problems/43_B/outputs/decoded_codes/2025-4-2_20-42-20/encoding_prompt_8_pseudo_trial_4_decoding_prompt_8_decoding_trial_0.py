def main():
    # Initialize Variables
    firstInput = input().replace(" ", "")
    secondInput = input().replace(" ", "")
    
    # Count Characters Frequency
    characterFrequencyDifference = []
    
    for char in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
        count_in_first = firstInput.count(chr(char))
        count_in_second = secondInput.count(chr(char))
        difference = count_in_first - count_in_second
        characterFrequencyDifference.append(difference)
    
    # Evaluate Results
    negative_count = sum(1 for diff in characterFrequencyDifference if diff < 0)
    
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the main function
main()
