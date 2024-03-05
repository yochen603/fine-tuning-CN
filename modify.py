def remove_newlines(input_file_path, output_file_path):
    try:
        # Open the input file and read its content
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove newline characters
        modified_content = content.replace('\n', '')

        # Write the modified content to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print("Newline characters removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_file_path = 'validation.txt'  # Path to your input file
output_file_path = 'validation_output.jsonl'  # Path to your output file
remove_newlines(input_file_path, output_file_path)
