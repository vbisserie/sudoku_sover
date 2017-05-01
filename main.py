puzzle_easy = [
    [7, None, None, 3, None, None, None, None, 9],
    [9, 3, None, None, 6, 4, 8, None, None],
    [None, 2, None, 5, 9, None, 4, None, 7],
    [2, None, 3, 6, None, 8, None, None, None],
    [None, 4, None, None, None, None, None, 8, None],
    [None, None, None, 4, None, 3, 9, None, 5],
    [3, None, 5, None, 1, 7, None, 9, None],
    [None, None, 2, 9, 3, None, None, 1, 8],
    [8, None, None, None, None, 5, None, None, 6],
]
puzzle_medium = [
    [None, 6, None, 7, None, None, 9, 8, None],
    [9, None, None, None, 1, 3, None, 7, 6],
    [None, None, None, None, 8, None, 5, None, None],
    [2, 1, None, None, 6, None, None, None, 3],
    [None, None, None, None, 3, None, None, None, None],
    [8, None, None, None, 5, None, None, 4, 2],
    [None, None, 2, None, 4, None, None, None, None],
    [5, 3, None, 2, 7, None, None, None, 9],
    [None, 8, 1, None, None, 6, None, 2, None],
]
puzzle_insane = [
    [2, None, 7, None, None, 5, None, 6, None],
    [None, None, None, 6, None, None, None, 1, 2],
    [None, None, 6, None, 1, None, None, None, None],
    [7, None, None, None, None, 2, None, None, None],
    [4, 8, None, None, None, None, None, 9, 1],
    [None, None, None, 8, None, None, None, None, 5],
    [None, None, None, None, 3, None, 8, None, None],
    [8, 7, None, None, None, 9, None, None, None],
    [None, 9, None, 5, None, None, 3, None, 4],
]
case_stack = []


def init_stack(puzzle):
    for x in range(0, 9):
        for y in range(0, 9):
            if type(puzzle[x][y]) is not int:
                puzzle[x][y] = range(1, 10)
                case_stack.append((x, y))


def feed_stack(puzzle, x, y):
    for i in range(0, 9):
        if i != x and type(puzzle[i][y]) is not int:
            case_stack.append((i, y))
    for j in range(0, 9):
        if j != y and type(puzzle[x][j]) is not int:
            case_stack.append((x, j))
    for i in range(0, 3):
        for j in range(0, 3):
            x_s = x - x % 3 + i
            y_s = y - y % 3 + j
            if x_s != x and y_s != y and type(puzzle[x_s][y_s]) is not int:
                case_stack.append((x_s, y_s))


def square_uniqueness_solution(puzzle, x, y):
    if type(puzzle[x][y]) is list:
        for v in puzzle[x][y]:
            is_the_only_place_for_v = True
            for i in range(0, 3):
                for j in range(0, 3):
                    x_s = x - x % 3 + i
                    y_s = y - y % 3 + j
                    if not (x_s == x and y_s == y) and \
                            ((type(puzzle[x_s][y_s]) is list and v in puzzle[x_s][y_s]) or
                                 (type(puzzle[x_s][y_s]) is int and v == puzzle[x_s][y_s])):
                        is_the_only_place_for_v = False
                        continue
                if not is_the_only_place_for_v:
                    continue
            if is_the_only_place_for_v:
                puzzle[x][y] = v
                print("Set {} to {}-{}".format(puzzle[x][y], x, y))
                feed_stack(puzzle, x, y)
                continue


def horizontal_uniqueness_solution(puzzle, x, y):
    if type(puzzle[x][y]) is list:
        for v in puzzle[x][y]:
            is_the_only_place_for_v = True
            for i in range(0, 9):
                if i != x and \
                        ((type(puzzle[i][y]) is list and v in puzzle[i][y]) or
                             (type(puzzle[i][y]) is int and puzzle[i][y] == v)):
                    is_the_only_place_for_v = False
                    continue
            if is_the_only_place_for_v:
                puzzle[x][y] = v
                print("Set {} to {}-{}".format(puzzle[x][y], x, y))
                feed_stack(puzzle, x, y)
                continue


def vertical_uniqueness_solution(puzzle, x, y):
    if type(puzzle[x][y]) is list:
        for v in puzzle[x][y]:
            is_the_only_place_for_v = True
            for j in range(0, 9):
                if j != y and \
                        ((type(puzzle[x][j]) is list and v in puzzle[x][j]) or
                             (type(puzzle[x][j]) is int and puzzle[x][j] == v)):
                    is_the_only_place_for_v = False
                    continue
            if is_the_only_place_for_v:
                puzzle[x][y] = v
                print("Set {} to {}-{}".format(puzzle[x][y], x, y))
                feed_stack(puzzle, x, y)
                continue


def check_case(puzzle, x, y):
    if len(puzzle[x][y]) is 1:
        puzzle[x][y] = puzzle[x][y][0]
        print("Set {} to {}-{}".format(puzzle[x][y], x, y))


def square_uniqueness_value(puzzle, x, y):
    if type(puzzle[x][y]) is list:
        for i in range(0, 3):
            for j in range(0, 3):
                x_s = x - x % 3 + i
                y_s = y - y % 3 + j
                if type(puzzle[x_s][y_s]) is int and puzzle[x_s][y_s] in puzzle[x][y]:
                    puzzle[x][y].remove(puzzle[x_s][y_s])
                    feed_stack(puzzle, x, y)
        check_case(puzzle, x, y)


def vertical_uniqueness_value(puzzle, x, y):
    if type(puzzle[x][y]) is list:
        for j in range(0, 9):
            if type(puzzle[x][j]) is int and puzzle[x][j] in puzzle[x][y]:
                puzzle[x][y].remove(puzzle[x][j])
                feed_stack(puzzle, x, y)
        check_case(puzzle, x, y)


def horizontal_uniqueness_value(puzzle, x, y):
    if type(puzzle[x][y]) is list:
        for i in range(0, 9):
            if type(puzzle[i][y]) is int and puzzle[i][y] in puzzle[x][y]:
                puzzle[x][y].remove(puzzle[i][y])
                feed_stack(puzzle, x, y)
        check_case(puzzle, x, y)


def solve(puzzle):
    init_stack(puzzle)
    while len(case_stack) > 0:
        x, y = case_stack.pop()
        vertical_uniqueness_value(puzzle, x, y)
        horizontal_uniqueness_value(puzzle, x, y)
        square_uniqueness_value(puzzle, x, y)
        vertical_uniqueness_solution(puzzle, x, y)
        horizontal_uniqueness_solution(puzzle, x, y)
        square_uniqueness_solution(puzzle, x, y)
    return puzzle


def print_puzzle(puzzle):
    for x in range(0, 9):
        line = ""
        for y in range(0, 9):
            if type(puzzle[x][y]) is int:
                line += "{}".format(puzzle[x][y])
            else:
                line += "."
            line += " "
            if (y+1) % 3 == 0:
                line += " "
        print(line)
        if (x+1) % 3 == 0:
            print("")


if __name__ == "__main__":
    print_puzzle(solve(puzzle_insane))
