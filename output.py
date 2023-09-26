# Import necessary modules
import sys
import logger
import utils
from Solution import SolutionAgent

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Initialize variables to store file path and grid string
    words_file_path = ''
    grid_string = ''

    # Check if the correct number of command-line arguments (2) are provided
    if len(sys.argv) == 3:
        words_file_path = sys.argv[1]  # The first argument is the words file path
        grid_string = sys.argv[2]      # The second argument is the grid string
    else:
        print("Wrong number of arguments")

    try:
        word_grid = grid_string

        # Check if the grid string has exactly 16 characters
        if len(word_grid) != 16:
            print("Wrong number of characters")
        # Check if the grid string contains only alphabetic characters
        elif not word_grid.isalpha():
            print("Character should only be alphabet")
        else:
            # Clean the original grid string
            original_grid = utils.clean_string(word_grid)

            # Convert the cleaned grid string to a structured grid
            structured_grid = utils.convert_to_structured(original_grid)

            # Initialize a solution agent
            solution_agent = SolutionAgent()

            # Read words from the specified file
            check_strings = utils.read_file_in(file_path=words_file_path)

            # Iterate through the words and check if they exist in the grid
            for word in check_strings:
                if solution_agent.exist(structured_grid, word):
                    print(word)

    except Exception as e:
        logger.error(e)
