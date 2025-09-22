def main():
    # Step 2: Initialize empty lists for processed input
    string_list1 = []
    string_list2 = []

    # Step 3: Take two input strings from the user
    input_string1 = input()
    input_string2 = input()

    # Step 4: Process each input string to remove spaces and store the results
    for character in input_string1:
        if character != ' ':
            string_list1.append(character)

    for character in input_string2:
        if character != ' ':
            string_list2.append(character)

    # Step 5: Initialize frequency difference list
    frequency_differences = []

    # Step 6: Calculate frequency differences for each character from 'A' to 'z'
    for value in range(ord('A'), ord('z') + 1):
        count_in_list1 = string_list1.count(chr(value))
        count_in_list2 = string_list2.count(chr(value))
        frequency_differences.append(count_in_list1 - count_in_list2)

    # Step 7: Check if all frequency differences are non-negative
    is_all_non_negative = True

    for frequency in frequency_differences:
        if frequency < 0:
            is_all_non_negative = False
            break

    # Step 8: Print the result based on frequency checks
    if is_all_non_negative:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
