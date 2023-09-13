import sys

def display_help():
    """Displays a help message."""
    help_message = """
Usage: text_tools.py [source_filename] <action>

Actions:
  --joiner     Joins lines from the source file.
  --dupes      Removes duplicate lines from the source file.

Options:
  source_filename    Specify the source file. If omitted, defaults to 'text.txt'.

Examples:
  text_tools.py --joiner
  text_tools.py source_filename.txt --dupes
  text_tools.py --help

Run without arguments to see this help message.
"""
    print(help_message)

def join_lines(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]
        joined_text = ' '.join(lines)

    with open(output_file, 'w') as f:
        f.write(joined_text)

def remove_duplicate_lines(input_file, output_file):
    seen = set()
    unique_lines = []

    with open(input_file, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line and stripped_line not in seen:
                seen.add(stripped_line)
                unique_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(unique_lines)

if __name__ == '__main__':
    # Default source file and action
    source_file = 'text.txt'
    destination_file = 'output.txt'
    action = None  # this will be either "joiner" or "dupes"

    if len(sys.argv) == 1 or '--help' in sys.argv:
        display_help()
    # Parse arguments
    for arg in sys.argv[1:]:
        if arg in ['--joiner', '--dupes']:
            action = arg[2:]
        else:
            source_file = arg

    # Determine the action to take based on the flag
    if action == "joiner":
        join_lines(source_file, destination_file)
        print(f"Lines from {source_file} have been joined and saved to {destination_file}.")
    elif action == "dupes":
        remove_duplicate_lines(source_file, destination_file)
        print(f"Duplicate lines from {source_file} have been removed and saved to {destination_file}.")
    else:
        print("Please specify a valid action using either --joiner or --dupes.")
