def normalize_path(input_path):
    """
    Normalize the input file path by removing redundant sections.
    
    Args:
        input_path (str): The path to be normalized.
    
    Returns:
        str: The normalized file path.
    """
    # Split the input path by slashes and filter out empty sections
    sections = [section for section in input_path.split('/') if section]
    
    # Join the sections back to a normalized path with a single slash
    normalized_path = '/' + '/'.join(sections)
    return normalized_path

def main():
    """
    The main function that drives the program.
    """
    # Step 1: Read the entire file path input from standard input
    file_path = input()
    
    # Step 2: Normalize the file path
    normalized_path = normalize_path(file_path)
    
    # Step 3: Ensure that the normalized path starts with a single forward slash
    if normalized_path.startswith('//'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Step 4: Output the final normalized path
    print(normalized_path)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
