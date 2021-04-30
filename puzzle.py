import random
from collections import defaultdict
from copy import deepcopy


def initial_grid():
    '''
    Generate a grid with first row filled with shuffled array from 1 to 9
    others filled with 0 that are undecided numbers
    :return:
    '''
    first_row = list(range(1, 10))
    random.shuffle(first_row)
    #first_row = [8, 4, 3, 7, 5, 9, 1, 6, 2] # for debug only
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
                print("==============================================================================\nOne grid generated")
                print(grid)
                # TODO: add 2 thermos and try to solve, if multiple solutions, add one more thermo until only one solution
                puzzle, known_cells = remove_numebrs(grid)
                copy_puzzle = deepcopy(puzzle)
                thermos = defaultdict(list)
                add_thermo(grid, thermos, known_cells)
                add_thermo(grid, thermos, known_cells)
                start_i, start_j = (0, 0)
                solutions = []
                while puzzle[start_i][start_j] != 0: # need start with an empty cell
                    start_i, start_j = next_cell(start_i, start_j)

                solve_puzzle(start_i, start_j, puzzle, thermos, solutions)
                while len(solutions)>1:
                    add_thermo(grid, thermos, known_cells)
                    solutions.clear()
                    solve_puzzle(start_i, start_j, puzzle, thermos, solutions)

                if len(solutions)==1:
                    print("---------------------------------------------------------------------")
                    print("Get one with just one solution!!!!!!!!!!!!!!!!!!!!!!!")
                    print("grid:\n", grid,"\npuzzle:\n", copy_puzzle, "\nsolutions:\n", solutions, "\nthermos:\n", thermos)
                    exit(0) # return doesn't work
            # else:
            #     print("not disjoint")
        generate_normal(grid, next_i, next_j)
        grid[i][j] = 0


def remove_numebrs(grid):
    '''
    for every row, we just keep 2 numbers, and we return a puzzle with only the 2*9 numbers, others filled with 0
    :param grid:
    :return: a new grid with only 18 known numbers and the coordinates of known cells
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
    known_cells = []
    for i in range(9):
        random.shuffle(col_indexes)
        col_0 = col_indexes[0]
        col_1 = col_indexes[1]
        col_2 = col_indexes[2]
        known_cells.append((i, col_0))
        known_cells.append((i, col_1))
        puzzle[i][col_0] = grid[i][col_0]
        puzzle[i][col_1] = grid[i][col_1]
        puzzle[i][col_2] = grid[i][col_2]

    return puzzle, known_cells


def solve_puzzle(i, j, puzzle, thermos, solutions):
    '''

    :param i: the row index of the next cell to fill
    :param j: the col index of the next cell to fill
    :param puzzle:
    :param thermos:
    :param solutions:
    :return:
    >>> p = [[0, 0, 0, 6, 0, 0, 8, 0, 0], [0, 2, 0, 0, 0, 0, 6, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 1], [2, 0, 0, 0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 4, 0, 0, 5], [0, 4, 0, 0, 9, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 0, 6, 0, 8, 0], [0, 0, 0, 0, 0, 7, 0, 0, 3]]
    >>> solve_puzzle(0, 0, p, {(1, 1): [((1, 2), (1, 3))]}, [])
    '''
    row_set = remains_in_row(i, puzzle)
    col_set = remains_in_col(j, puzzle)
    subgrid_set = remains_in_subgrid(i, j, puzzle)
    remains_set = row_set & col_set & subgrid_set
    remains_list = sorted(list(remains_set))
    for element in remains_list:
        puzzle[i][j] = element
        next_i, next_j = next_cell(i, j)
        while next_i!=-1 and puzzle[next_i][next_j] != 0:
            next_i, next_j = next_cell(next_i, next_j)

        if next_i == -1: # all the cells are filled
            # print("all the cells are filled")
            if is_disjoint(puzzle) and satisfy_thermos(puzzle, thermos):
                one_solution = deepcopy(puzzle)
                print("one solution generated!\n", one_solution)
                solutions.append(one_solution)
                if len(solutions)> 1: # already has a solution
                    print("has more than one solution!")
                    puzzle[i][j] = 0
                    return False
        else:
            if not solve_puzzle(next_i, next_j, puzzle, thermos, solutions):
                return False
    puzzle[i][j] = 0
    return True


def satisfy_thermos(puzzle, thermos):
    '''
    see if all filled puzzle satisfy all the thermos constaints
    :param puzzle:
    :param thermos:
    :return:
    >>> good_grid = [[1, 5, 7, 6, 4, 3, 8, 2, 9]]
    >>> good_grid.append([9, 2, 3, 8, 5, 1, 6, 4, 7])
    >>> good_grid.append([8, 6, 4, 7, 2, 9, 5, 3, 1])
    >>> good_grid.append([2, 3, 1, 5, 7, 8, 4, 9, 6])
    >>> good_grid.append([7, 9, 8, 3, 6, 4, 2, 1, 5])
    >>> good_grid.append([6, 4, 5, 1, 9, 2, 3, 7, 8])
    >>> good_grid.append([3, 1, 2, 9, 8, 5, 7, 6, 4])
    >>> good_grid.append([5, 7, 9, 4, 3, 6, 1, 8, 2])
    >>> good_grid.append([4, 8, 6, 2, 1, 7, 9, 5, 3])
    >>> thermos = {(1, 1): [((1, 2), (1, 3))], (4, 5): [((3, 5), (2, 5))], (2, 8): [((1, 8), (0, 8)), ((2, 7), (2, 6))]}
    >>> satisfy_thermos(good_grid, thermos)
    True
    '''
    for bulb in thermos:
        bulb_i, bulb_j = bulb
        # print(bulb)
        for cells in thermos[bulb]:
            # print(cells)
            cell1_i, cell1_j = cells[0]
            cell2_i, cell2_j = cells[1]
            if not (puzzle[bulb_i][bulb_j] < puzzle[cell1_i][cell1_j] and puzzle[cell1_i][cell1_j] < puzzle[cell2_i][cell2_j]):
                return False
    return True


def add_thermo(grid, thermos, known_cells):
    '''

    :param grid:
    :param thermos: thermo only starts with known cells, , every thermo is of length 3
    one known cell can be the bulbs of multiple thermos, and sure it can just have at most 4 thermos starting from it
    format of thermos: {(1, 1): [((1, 2), (1, 3))], (4, 5): [((3, 5), (2, 5))], (2, 8): [((1, 8), (0, 8)), ((2, 7), (2, 6))]}
    :param known_cells:
    :return:
    >>> good_grid = [[1, 5, 7, 6, 4, 3, 8, 2, 9]]
    >>> good_grid.append([9, 2, 3, 8, 5, 1, 6, 4, 7])
    >>> good_grid.append([8, 6, 4, 7, 2, 9, 5, 3, 1])
    >>> good_grid.append([2, 3, 1, 5, 7, 8, 4, 9, 6])
    >>> good_grid.append([7, 9, 8, 3, 6, 4, 2, 1, 5])
    >>> good_grid.append([6, 4, 5, 1, 9, 2, 3, 7, 8])
    >>> good_grid.append([3, 1, 2, 9, 8, 5, 7, 6, 4])
    >>> good_grid.append([5, 7, 9, 4, 3, 6, 1, 8, 2])
    >>> good_grid.append([4, 8, 6, 2, 1, 7, 9, 5, 3])
    >>> grid = [[0, 0, 0, 6, 0, 0, 8, 0, 0], [0, 2, 0, 0, 0, 0, 6, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 1], [2, 0, 0, 0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 4, 0, 0, 5], [0, 4, 0, 0, 9, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 0, 6, 0, 8, 0], [0, 0, 0, 0, 0, 7, 0, 0, 3]]
    >>> known_cells = [(0, 6), (0, 3), (1, 6), (1, 1), (2, 4), (2, 8), (3, 0), (3, 8), (4, 5), (4, 8), (5, 4), (5, 1), (6, 2), (6, 6), (7, 5), (7, 7), (8, 8), (8, 5)]
    >>> thermos = defaultdict(list)
    >>> add_thermo(good_grid, thermos, known_cells)
    >>> add_thermo(good_grid, thermos, known_cells)
    >>> add_thermo(good_grid, thermos, known_cells)
    >>> add_thermo(good_grid, thermos, known_cells)
    >>> all([bulb in known_cells for bulb in thermos.keys()])
    True
    '''
    random.shuffle(known_cells)
    for index in known_cells:
        i, j = index

        if grid[i][j] > 7: # impossible for a length of 3 thermo
            continue
        # go upward
        if i>1 and grid[i][j]< grid[i-1][j] and grid[i-1][j]< grid[i-2][j]:
            if index not in thermos or ((i-1, j), (i-2, j)) not in thermos[index]:
                thermos[index].append(((i-1, j), (i-2, j)))
                break

        # go downward
        if i<7 and grid[i][j]< grid[i+1][j] and grid[i+1][j] < grid[i+2][j]:
            if index not in thermos or ((i+1, j), (i+2, j)) not in thermos[index]:
                thermos[index].append(((i+1, j), (i+2, j)))
                break

        # go right
        if j<7 and grid[i][j]< grid[i][j+1] and grid[i][j+1] < grid[i][j+2]:
            if index not in thermos or ((i, j+1), (i, j+2)) not in thermos[index]:
                thermos[index].append(((i, j+1), (i, j+2)))
                break

        # go left
        if j>1 and grid[i][j]< grid[i][j-1] and grid[i][j-1] < grid[i][j-2]:
            if index not in thermos or ((i, j-1), (i, j-2)) not in thermos[index]:
                thermos[index].append(((i, j-1), (i, j-2)))
                break

    print("Current thermos: ", thermos)


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
