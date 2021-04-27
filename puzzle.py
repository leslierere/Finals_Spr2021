import random

def initial_grid():
    '''
    Generate a grid with first row filled with shuffled array from 1 to 9
    others filled with 0 that are undecided numbers
    :return:
    '''
    # first_row = list(range(1, 10))
    # random.shuffle(first_row)
    first_row = [8, 4, 3, 7, 5, 9, 1, 6, 2]
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for j in range(9):
        grid[0][j] = first_row[j]

    return grid

def generate_normal(first_row, grid):
    pass


def remains_in_row(i, grid):
    '''
    return a set of available numbers in the row
    :param i:
    :param grid:
    :return:
    >>> grid = [[8, 4, 3, 7, 5, 9, 1, 6, 2], [0, 4, 3, 0, 5, 9, 0, 6, 0]]
    >>> remains_in_row(1, grid) == {1, 2, 7, 8}
    True
    '''
    row_set = set(grid[i])
    return set(list(range(1, 10))) - row_set


def remains_in_col(j, grid):
    '''
    return a set of available numbers in the column
    :param i:
    :param grid:
    :return:
    >>> grid = [[3, 0, 9, 0, 0, 0, 0, 0, 2]]
    >>> grid.append([0, 0, 0, 0, 3, 2, 1, 0, 8])
    >>> grid.append([4, 1, 0, 0, 0, 0, 8, 0, 0])
    >>> grid.append([0, 2, 0, 9, 0, 0, 0, 0, 0])
    >>> grid.append([0, 0, 7, 3, 0, 1, 5, 0, 0])
    >>> grid.append([0, 0, 0, 0, 0, 5, 0, 6, 0])
    >>> grid.append([0, 0, 3, 0, 0, 0, 0, 8, 5])
    >>> grid.append([7, 0, 5, 1, 6, 0, 0, 0, 0])
    >>> grid.append([6, 0, 0, 0, 0, 0, 9, 0, 7])
    >>> remains_in_col(2, grid) == {1, 2, 4, 6, 8}
    True
    '''
    col_set = set(row[j] for row in grid)
    return set(list(range(1, 10))) - col_set


def remains_in_subgrid(i, j, grid):
    '''
    return a set of available numbers in the subgrid
    :param i:
    :param j:
    :param grid:
    :return:
    >>> grid = [[3, 0, 9, 0, 0, 0, 0, 0, 2]]
    >>> grid.append([0, 0, 0, 0, 3, 2, 1, 0, 8])
    >>> grid.append([4, 1, 0, 0, 0, 0, 8, 0, 0])
    >>> grid.append([0, 2, 0, 9, 0, 0, 0, 0, 0])
    >>> grid.append([0, 0, 7, 3, 0, 1, 5, 0, 0])
    >>> grid.append([0, 0, 0, 0, 0, 5, 0, 6, 0])
    >>> grid.append([0, 0, 3, 0, 0, 0, 0, 8, 5])
    >>> grid.append([7, 0, 5, 1, 6, 0, 0, 0, 0])
    >>> grid.append([6, 0, 0, 0, 0, 0, 9, 0, 7])
    >>> remains_in_subgrid(1, 1, grid) == {2, 5, 6, 7, 8}
    True
    >>> remains_in_subgrid(6, 3, grid) == {2, 3, 4, 5, 7, 8, 9}
    True
    >>> remains_in_subgrid(8, 2, grid) == {1, 2, 4, 8, 9}
    True
    '''
    start_i = i//3 * 3
    start_j = j//3 * 3
    subgrid = []

    for row_idx in range(start_i, start_i+3):
        for col_idx in range(start_j, start_j+3):
            subgrid.append(grid[row_idx][col_idx])

    return set(list(range(1, 10))) - set(subgrid)


if __name__ == '__main__':
    grid = initial_grid()
    print(grid)
