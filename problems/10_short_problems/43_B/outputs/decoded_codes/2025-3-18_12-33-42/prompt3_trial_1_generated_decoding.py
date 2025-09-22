def compare_string_frequencies():
    # Input two strings and remove spaces
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")

    # Create a list to store frequency differences of character counts
    frequency_differences = []

    # Iterate over the ASCII range from 'A' (65) to 'z' (122)
    for char_code in range(ord('A'), ord('z') + 1):
        character = chr(char_code)

        # Count occurrences of the character in both strings
        count_in_first_string = first_string.count(character)
        count_in_second_string = second_string.count(character)

        # Calculate the difference in frequencies and store it
        frequency_difference = count_in_first_string - count_in_second_string
        frequency_differences.append(frequency_difference)

    # Check if any frequency differences are negative
    negative_count = sum(1 for diff in frequency_differences if diff < 0)

    # Print "YES" if there are no negative differences, otherwise print "NO"
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the program
compare_string_frequencies()


  A B
  A B
  

  AAB
  BAA
  

  AAB
  BB
  