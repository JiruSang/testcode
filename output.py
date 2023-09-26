import sys
import logger
import utils
from Solution import SolutionAgent

if __name__ == '__main__':
    words_file_path = ''
    grid_string = ''
    if len(sys.argv) == 3:
        words_file_path = sys.argv[1]
        grid_string = sys.argv[2]

    else:
        print("Wrong number of arguments")
    try:
        word_grid = grid_string
        if len(word_grid) != 16:
            print("Wrong number of characters")
        elif not word_grid.isalpha():
            print("Character should only be alphabet")
        else:
            original_grid = utils.clean_string(word_grid)
            structured_grid = utils.convert_to_structured(original_grid)
            solution_agent = SolutionAgent()

            check_strings = utils.read_file_in(file_path = words_file_path)
            for word in check_strings:
                if solution_agent.exist(structured_grid, word):
                    print(word)

    except Exception as e:
        logger.error(e)
