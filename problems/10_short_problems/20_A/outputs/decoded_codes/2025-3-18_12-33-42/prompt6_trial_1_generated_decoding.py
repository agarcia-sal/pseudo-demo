def normalize_path(potential_path):
    # Replace any occurrences of multiple slashes with a single slash
    modified_path = '/'.join(filter(None, potential_path.split('/')))
    return modified_path

def main():
    # Read input from standard input and remove leading/trailing spaces
    input_string = input().strip()
    
    # Normalize the path to use the appropriate format
    normalized_path = normalize_path(input_string)
    
    # Replace any sequence of leading slashes with a single slash
    adjusted_path = '/' + normalized_path.lstrip('/')
    
    # Output the adjusted path
    print(adjusted_path)

# To execute the main function
if __name__ == "__main__":
    main()
