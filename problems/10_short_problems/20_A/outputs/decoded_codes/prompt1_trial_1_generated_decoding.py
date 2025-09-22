def normaliza_path(path):
    # This should contain logic to standardize the path format
    # For demonstration, we will just return the path as is.
    # In a real scenario, implement the required normalization.
    return path

def remove_leading_slashes(path):
    # Check if the path starts with '/'
    if path.startswith('/'):
        # Find the index of the first non-slash character
        first_non_slash_index = 0
        while first_non_slash_index < len(path) and path[first_non_slash_index] == '/':
            first_non_slash_index += 1
            
        # Return the path with a single leading slash
        return '/' + path[first_non_slash_index:]
    else:
        # Return the path unchanged
        return path

# Begin main logic
input_string = input()  # Read input from standard input
cleaned_string = input_string.strip()  # Trim whitespace

normalized_path = normaliza_path(cleaned_string)  # Normalize the path
final_path = remove_leading_slashes(normalized_path)  # Remove leading slashes

print(final_path)  # Output the final formatted path
