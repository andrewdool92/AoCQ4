
class Grid:
    def __init__(self, filename: str, keyword: str):
        self.grid: [str] = read_file(filename)
        self.keyword = keyword.upper()

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])       # assumes all rows are of equal length

    def _check_word(self, row: int, col: int, word: str) -> int:
        """
        search for the given word in the right, down, right-down, and right-up diagonal directions of start index
        I'm searching the grid right-to-left, top-to-bottom, so words in other directions will already have been found

        :param row:
        :param col:
        :param word:
        :return: number of instances of search word found that start on the given coordinates
        """
        if not word.startswith(self.grid[row][col]):
            return 0

        count: int = 0

        for move in [[1, 0], [1, 1], [0, 1], [-1, 1]]:
            found = True

            for char_idx in range(1, len(word)):
                check_row = row + move[0] * char_idx
                check_col = col + move[1] * char_idx

                in_bounds = 0 <= check_row < self.rows and 0 <= check_col < self.cols

                if not in_bounds or self.grid[check_row][check_col] != word[char_idx]:
                    found = False
                    break

            if found:
                count += 1

        return count

    def _check_char(self, row: int, col: int):
        """
        check for the keyword and the reversed keyword starting from the given coordinates

        :param row:
        :param col:
        :return: number of instances of search word found that start/end on the given coordinates
        """
        count = 0

        for word in [self.keyword, self.keyword[::-1]]:
            count += self._check_word(row, col, word)

        return count

    def find_word_count(self) -> int:
        """
        evaluate the puzzle for instances of the keyword

        :return: number of keyword instances found
        """
        word_count = 0

        for row in range(self.rows):
            for col in range(self.cols):
                word_count += self._check_char(row, col)

        return word_count


def read_file(filename: str) -> [str]:
    """
    read puzzle input from a text file

    :param filename:
    :return: a list of each line of the puzzle
    """
    grid = []

    file = open(filename)
    while line := file.readline():
        grid.append(line.strip())

    return grid


if __name__ == "__main__":
    word: str = 'XMAS'

    puzzle = Grid('puzzle.txt', word)
    print(f'The word {word} appears {puzzle.find_word_count()} times')
