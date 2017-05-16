class Puzzle(object):
    def __init__(self):
        self.puzzle = [None] * 9
        for x in range(0, 9):
            self.puzzle[x] = []
            for y in range(0, 9):
                self.puzzle[x].append(range(1, 10))

    def copy(self, puzzle):
        for x in range(0, 9):
            for y in range(0, 9):
                if type(puzzle.get_value(x, y)) is list:
                    self.puzzle[x][y] = []
                    for v in puzzle.get_value(x, y):
                        self.puzzle[x][y].append(v)
                else:
                    self.puzzle[x][y] = puzzle.get_value(x, y)

    def show(self):
        for x in range(0, 9):
            line = ""
            for y in range(0, 9):
                if type(self.puzzle[x][y]) is int:
                    line += "{}".format(self.puzzle[x][y])
                else:
                    line += "."
                line += " "
                if (y + 1) % 3 == 0:
                    line += " "
            print(line)
            if (x + 1) % 3 == 0:
                print("")

    def check_values(self):
        for x in range(0, 9):
            for y in range(0, 9):
                if not self.check_value(x, y, self.puzzle[x][y]):
                    return False
        return True

    def check_value(self, x, y, v):
        for i in range(0, 9):
            if i != x and type(self.puzzle[i][y]) is int and self.puzzle[i][y] == v:
                return False
        for j in range(0, 9):
            if j != y and type(self.puzzle[x][j]) is int and self.puzzle[x][j] == v:
                return False
        for i in range(0, 3):
            x_s = x - x % 3 + i
            for j in range(0, 3):
                y_s = y - y % 3 + j
                if not (x_s == x and y_s == y) and type(self.puzzle[x_s][y_s]) is int and self.puzzle[x_s][y_s] == v:
                    return False
        return True

    def remove_value(self, x, y, v):
        if type(self.puzzle[x][y]) is list and v in self.puzzle[x][y]:
            self.puzzle[x][y].remove(v)
            if len(self.puzzle[x][y]) == 1:
                self.set_value(x, y, self.puzzle[x][y][0])

    def set_value(self, x, y, v):
        if self.check_value(x, y, v):
            self.puzzle[x][y] = v
            for i in range(0, 9):
                if i != x:
                    self.remove_value(i, y, v)
            for j in range(0, 9):
                if j != y:
                    self.remove_value(x, j, v)
            for i in range(0, 3):
                x_s = x - x % 3 + i
                for j in range(0, 3):
                    y_s = y - y % 3 + j
                    if not (x_s == x and y_s == y):
                        self.remove_value(x_s, y_s, v)
            return True
        else:
            return False

    def get_value(self, x, y):
        if x in range(0, 9) and y in range(0, 9):
            return self.puzzle[x][y]
        return None

    def _recursively_solve(self, x, y):
        if x not in range(0, 9) or y not in range(0, 9):
            return False
        if x == 8 and y == 8:
            return self.check_value(x, y, self.puzzle[x][y])

        x_n1 = x + 1
        y_n1 = y
        if x_n1 == 9:
            x_n1 = 0
            y_n1 += 1
        if type(self.puzzle[x][y]) is int:
            return self._recursively_solve(x_n1, y_n1)
        else:
            for v in self.puzzle[x][y]:
                puzzle_n1 = Puzzle()
                puzzle_n1.copy(self)
                if puzzle_n1.set_value(x, y, v):
                    if puzzle_n1._recursively_solve(x_n1, y_n1):
                        self.copy(puzzle_n1)
                        return True
        return False

    def solve(self):
        return self._recursively_solve(0, 0)
