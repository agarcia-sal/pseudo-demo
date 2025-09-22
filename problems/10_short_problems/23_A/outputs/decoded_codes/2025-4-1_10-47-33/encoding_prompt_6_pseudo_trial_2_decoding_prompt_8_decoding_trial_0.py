def find_longest_repeated_substring():
    line = input()
    length_of_line = len(line)
    longest_repeated_length = 0

    for current_length in range(1, length_of_line):  # start from 1 to avoid empty substring
        for start_index in range(length_of_line - current_length):  # adjust to avoid overflow
            substring = line[start_index:start_index + current_length]

            if substring in line[start_index + 1:]:
                longest_repeated_length = current_length
                break  # exit inner loop if a repeat is found

    print(longest_repeated_length)
