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


def generate_normal(grid, i, j):
    row_set = remains_in_row(i, grid)
    col_set = remains_in_col(j, grid)
    subgrid_set = remains_in_subgrid(i, j, grid)
    remains_set = row_set&col_set&subgrid_set
    remains_list = list(remains_set)
    for element in remains_list:
        grid[i][j] = element
        next_i, next_j = next_cell(i, j)
        if next_i == -1:
            if is_disjoint(grid):
                print(grid)
            # else:
            #     print("not disjoint")
        generate_normal(grid, next_i, next_j)
        grid[i][j] = 0


def remove_numebrs(grid):
    '''
    for every row, we just keep 2 numbers, and we return a puzzle with only the 2*9 numbers, others filled with 0
    :param grid:
    :return: a new grid with only 18 known numbers
    >>> good_grid = [[1, 5, 7, 6, 4, 3, 8, 2, 9]]
    >>> good_grid.append([9, 2, 3, 8, 5, 1, 6, 4, 7])
    >>> good_grid.append([8, 6, 4, 7, 2, 9, 5, 3, 1])
    >>> good_grid.append([2, 3, 1, 5, 7, 8, 4, 9, 6])
    >>> good_grid.append([7, 9, 8, 3, 6, 4, 2, 1, 5])
    >>> good_grid.append([6, 4, 5, 1, 9, 2, 3, 7, 8])
    >>> good_grid.append([3, 1, 2, 9, 8, 5, 7, 6, 4])
    >>> good_grid.append([5, 7, 9, 4, 3, 6, 1, 8, 2])
    >>> good_grid.append([4, 8, 6, 2, 1, 7, 9, 5, 3])
    >>> remove_numebrs(good_grid)
    '''
    puzzle = [[0 for _ in range(9)] for _ in range(9)]
    col_indexes = [i for i in range(9)]
    for i in range(9):
        random.shuffle(col_indexes)
        col_0 = col_indexes[0]
        col_1 = col_indexes[1]
        puzzle[i][col_0] = grid[i][col_0]
        puzzle[i][col_1] = grid[i][col_1]

    return puzzle


def solve_puzzle(grid, thermos):
    '''

    :param grid:
    :param thermos:
    :return:
    >>> grid = [[0, 0, 0, 0, 0, 3, 0, 2, 0], [0, 2, 0, 0, 0, 0, 0, 4, 0], [8, 0, 0, 0, 0, 0, 5, 0, 0], [2, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 8, 0, 0, 4, 0, 0, 0], [6, 4, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 6, 0], [5, 0, 0, 0, 0, 6, 0, 0, 0], [0, 8, 6, 0, 0, 0, 0, 0, 0]]
    '''

def next_cell(i, j):
    '''
    Given the cell which is just filled with a number, find the next cell to fill, and we will fill row by row
    :param i:
    :param j:
    :return:
    >>> next_cell(0, 0)
    (0, 1)
    >>> next_cell(0, 8)
    (1, 0)
    >>> next_cell(8, 8)
    (-1, -1)
    '''
    row_j = j+1
    row_i = i
    if row_j==9:
        row_j = 0
        row_i+=1
    if row_i==9:
        return (-1, -1)
    return (row_i, row_j)


def is_disjoint(grid):
    '''

    :param grid:
    :return: true if this grid satisfy disjoint set
    >>> grid = [[8, 4, 3, 7, 5, 9, 1, 6, 2], [1, 2, 9, 8, 3, 6, 4, 5, 7], [5, 6, 7, 1, 2, 4, 8, 9, 3], [2, 1, 8, 3, 9, 5, 6, 7, 4], [3, 9, 6, 2, 4, 7, 5, 1, 8], [4, 7, 5, 6, 1, 8, 2, 3, 9], [7, 8, 4, 5, 6, 3, 9, 2, 1], [9, 5, 1, 4, 7, 2, 3, 8, 6], [6, 3, 2, 9, 8, 1, 7, 4, 5]]
    >>> is_disjoint(grid)
    False
    >>> good_grid = [[1, 5, 7, 6, 4, 3, 8, 2, 9]]
    >>> good_grid.append([9, 2, 3, 8, 5, 1, 6, 4, 7])
    >>> good_grid.append([8, 6, 4, 7, 2, 9, 5, 3, 1])
    >>> good_grid.append([2, 3, 1, 5, 7, 8, 4, 9, 6])
    >>> good_grid.append([7, 9, 8, 3, 6, 4, 2, 1, 5])
    >>> good_grid.append([6, 4, 5, 1, 9, 2, 3, 7, 8])
    >>> good_grid.append([3, 1, 2, 9, 8, 5, 7, 6, 4])
    >>> good_grid.append([5, 7, 9, 4, 3, 6, 1, 8, 2])
    >>> good_grid.append([4, 8, 6, 2, 1, 7, 9, 5, 3])
    >>> is_disjoint(good_grid)
    True
    '''
    for i in range(0, 3):
        for j in range(0, 3):
            element = grid[i][j]
            for d_i in range(3):
                for d_j in range(3):
                    if d_i==0 and d_j ==0:
                        continue
                    if grid[i+d_i*3][j+d_j*3] == element:
                        # print(i, j, i+ d_i, j + d_j, element)
                        return False
    return True


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
    generate_normal(grid, 1, 0)
    # print(grid)
