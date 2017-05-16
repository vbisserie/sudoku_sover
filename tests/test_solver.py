import pytest

from services.puzzle import Puzzle

headers = {'Content-Type': 'application/json'}


@pytest.fixture(params=[
    [
        [7, None, None, 3, None, None, None, None, 9],
        [9, 3, None, None, 6, 4, 8, None, None],
        [None, 2, None, 5, 9, None, 4, None, 7],
        [2, None, 3, 6, None, 8, None, None, None],
        [None, 4, None, None, None, None, None, 8, None],
        [None, None, None, 4, None, 3, 9, None, 5],
        [3, None, 5, None, 1, 7, None, 9, None],
        [None, None, 2, 9, 3, None, None, 1, 8],
        [8, None, None, None, None, 5, None, None, 6],
    ], [
        [None, 6, None, 7, None, None, 9, 8, None],
        [9, None, None, None, 1, 3, None, 7, 6],
        [None, None, None, None, 8, None, 5, None, None],
        [2, 1, None, None, 6, None, None, None, 3],
        [None, None, None, None, 3, None, None, None, None],
        [8, None, None, None, 5, None, None, 4, 2],
        [None, None, 2, None, 4, None, None, None, None],
        [5, 3, None, 2, 7, None, None, None, 9],
        [None, 8, 1, None, None, 6, None, 2, None],
    ], [
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
])
def data_for_test(request):
    return request.param


def test_solver(data_for_test):
    puzzle = Puzzle()
    for x in range(0, 9):
        for y in range(0, 9):
            if type(data_for_test[x][y]) is int:
                puzzle.set_value(x, y, data_for_test[x][y])
    assert puzzle.solve() is True
    assert puzzle.check_values() is True
    puzzle.show()
