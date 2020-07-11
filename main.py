import itertools

import pandas as pd

##breezy
# solvable with pencil rows and columns and fill one_pencil
r1 = [3, 0, 1, 0, 0, 6, 7, 8, 9]
r2 = [0, 2, 4, 0, 9, 8, 1, 5, 0]
r3 = [9, 8, 7, 5, 1, 3, 4, 0, 2]
r4 = [4, 6, 9, 0, 7, 5, 2, 1, 8]
r5 = [0, 1, 8, 0, 4, 9, 0, 0, 5]
r6 = [2, 3, 5, 0, 6, 1, 9, 4, 7]
r7 = [1, 7, 3, 6, 5, 2, 8, 0, 4]
r8 = [0, 9, 2, 0, 8, 4, 3, 7, 0]
r9 = [8, 0, 6, 0, 0, 7, 5, 2, 1]
test1 = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

##easy
r1 = [0, 6, 2, 0, 0, 0, 3, 4, 0]
r2 = [8, 0, 4, 0, 0, 0, 2, 0, 5]
r3 = [1, 9, 0, 0, 5, 0, 0, 6, 7]
r4 = [0, 0, 0, 5, 0, 7, 0, 0, 0]
r5 = [0, 0, 6, 0, 3, 0, 7, 0, 0]
r6 = [0, 0, 0, 6, 0, 2, 0, 0, 0]
r7 = [3, 2, 0, 0, 4, 0, 0, 7, 1]
r8 = [7, 0, 1, 0, 0, 0, 5, 0, 4]
r9 = [0, 4, 5, 0, 0, 0, 9, 2, 0]
test2 = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

r1 = [0, 3, 4, 7, 0, 5, 1, 6, 0]
r2 = [8, 6, 0, 0, 0, 0, 0, 5, 3]
r3 = [1, 0, 0, 6, 8, 3, 0, 0, 4]
r4 = [5, 0, 8, 0, 1, 0, 6, 0, 2]
r5 = [0, 0, 1, 8, 0, 2, 7, 0, 0]
r6 = [3, 0, 9, 0, 6, 0, 8, 0, 1]
r7 = [7, 0, 0, 2, 5, 1, 0, 0, 6]
r8 = [4, 1, 0, 0, 0, 0, 0, 2, 9]
r9 = [0, 8, 5, 4, 0, 6, 3, 1, 0]
test3 = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

# medium
r1 = [0, 0, 0, 0, 0, 0, 0, 2, 0]
r2 = [0, 8, 0, 0, 0, 6, 0, 0, 7]
r3 = [0, 0, 0, 3, 0, 1, 0, 0, 0]
r4 = [7, 0, 0, 0, 1, 0, 8, 4, 0]
r5 = [0, 6, 9, 7, 0, 4, 0, 0, 0]
r6 = [0, 0, 0, 0, 6, 0, 5, 0, 0]
r7 = [2, 5, 0, 0, 3, 0, 0, 0, 0]
r8 = [3, 0, 8, 0, 7, 0, 0, 1, 0]
r9 = [9, 7, 6, 0, 0, 8, 0, 0, 0]
test4 = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

r1 = [0, 0, 7, 8, 0, 9, 6, 0, 0]
r2 = [8, 0, 9, 0, 0, 0, 3, 0, 7]
r3 = [6, 5, 0, 0, 0, 0, 0, 2, 9]
r4 = [1, 0, 0, 7, 0, 4, 0, 0, 6]
r5 = [9, 0, 0, 0, 0, 0, 0, 0, 1]
r6 = [0, 0, 6, 0, 0, 0, 9, 0, 0]
r7 = [0, 7, 4, 0, 6, 0, 5, 3, 0]
r8 = [0, 9, 0, 2, 0, 3, 0, 6, 0]
r9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
test5 = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

# hard
r1 = [0, 0, 0, 0, 9, 4, 0, 0, 8]
r2 = [0, 0, 0, 0, 1, 8, 2, 9, 0]
r3 = [0, 0, 0, 0, 0, 7, 0, 0, 4]
r4 = [0, 0, 0, 0, 0, 0, 0, 3, 0]
r5 = [2, 6, 0, 0, 0, 0, 1, 0, 7]
r6 = [1, 3, 7, 0, 0, 0, 0, 0, 9]
r7 = [0, 5, 0, 0, 4, 0, 3, 0, 0]
r8 = [0, 8, 0, 7, 0, 0, 0, 0, 0]
r9 = [9, 0, 4, 0, 2, 3, 0, 0, 0]
test6 = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

# debug
r1 = [0, 0, 0, 1, 3, 4, 6, 2, 5]
r2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r4 = [0, 7, 0, 0, 0, 0, 0, 0, 0]
r5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r6 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r7 = [0, 0, 7, 0, 0, 0, 0, 0, 0]
r8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
debug1 = [r1, r2, r3, r4, r5, r6, r7, r8, r9]


def countDuplicate(listOfElems):
    ''' Check if given list contains any duplicates '''
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems and elem != 0:
            return 1
        else:
            setOfElems.add(elem)
    return 0


def checkDuplicate(listOfElems):
    ''' Check if given list contains any duplicates '''
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return 1
        else:
            setOfElems.add(elem)
    return 0


class Cell:
    def __init__(self):
        self.num = 0
        self.pencil = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num

    def get_pencil(self):
        return self.pencil

    def mod_pencil(self, rm_list):
        for num in rm_list:
            if num in self.pencil:
                self.pencil.remove(num)

    def clear_pencils(self):
        self.pencil = [self.num]


class Box:
    """
    0 1 2
    3 4 5
    6 7 8
    """

    def __init__(self, box_num):
        self.cells = []
        self.nums = []

    def add_cell(self, cell):
        self.cells.append(cell)
        self.nums.append(cell.get_num())

    def update_cells(self):
        self.nums = [cell.get_num() for cell in self.cells]

    def get_nums(self):
        return self.nums

    def __getitem__(self, key):
        return self.cells[key]


class Grid:
    def __init__(self, knowns):
        self.knowns = knowns
        tot = []
        for i, row in enumerate(self.knowns):
            new_row = []
            for j, col in enumerate(row):
                self.__dict__[f'r{i}c{j}'] = Cell()
                self.__dict__[f'r{i}c{j}'].set_num(col)
                new_row.append(self.__dict__[f'r{i}c{j}'])
            tot.append(new_row)
        self.df = pd.DataFrame(tot)

    def create_boxes(self):
        for i in range(9):
            self.__dict__[f'_box{i}'] = Box(i)

    def fill_boxes(self):
        """
        r = first row,
        c = first col
        0: r012, c012
        1: r012, c345
        2: r012, c678
        :return:
        """
        for b in range(9):
            r = b // 3 * 3
            c = b % 3 * 3
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    self.__dict__[f'_box{b}'].add_cell(self.df.iloc[i][j])

    def update_boxes(self):
        for b in range(9):
            self.__dict__[f'_box{b}'].update_cells()

    def clear_pencils(self):
        for i in range(9):
            for j in range(9):
                cell = self.df.iloc[i][j]
                if cell.get_num() != 0:
                    cell.clear_pencils()

    def find_pencil(self, digit, list_num, list_type):
        pen_positions = []
        for i in range(9):
            if list_type == 'row':
                cell_pens = self.df.iloc[list_num][i].get_pencil()
            elif list_type == 'col':
                cell_pens = self.df[list_num][i].get_pencil()
            else:
                cell_pens = self.__dict__[f'_box{list_num}'][i].get_pencil()
            if digit in cell_pens:
                pen_positions.append(i)
        return pen_positions

    def pencil_basic(self, list_type):
        for i in range(9):
            if list_type == 'row':
                cell_list = self.df.iloc[i]
            elif list_type == 'col':
                cell_list = self.df[i]
            else:
                cell_list = self.__dict__[f'_box{i}']

            list_string = [cell_list[j].get_num() for j in range(9)]
            for c in cell_list:
                if c.get_num() == 0:
                    c.mod_pencil(list_string)

    def identify_pair(self, list_type):
        """
        [12, 12, 123]
        x number for x squares
        for i in range(9):
            if num pencils = 2
                potensh_pair = pencils
                for j in range(9) and not i
                    if pencisl = potensh_pair
                        for k in range(9)
                            if not i or j
                                rm(pair)

        :return:
        """
        for list_num in range(9):
            if list_type == 'row':
                cell_list = self.df.iloc[list_num]
            elif list_type == 'col':
                cell_list = self.df[list_num]
            else:
                cell_list = self.__dict__[f'_box{list_num}']
            for i in range(9):
                pens = cell_list[i].get_pencil()
                if len(pens) == 2:
                    pair = pens
                    for j in range(9):
                        pens2 = cell_list[j].get_pencil()
                        if j != i and pens2 == pair:
                            self.rm_pair(pair, [i, j], cell_list)

    def rm_pair(self, pair, pair_location, list_num):
        for i in range(9):
            if i not in pair_location:
                list_num[i].mod_pencil(pair)

    def fill_one_pencil(self):
        for i in range(9):
            for j in range(9):
                cell_ = self.df[i][j]
                pen = cell_.get_pencil()
                if len(pen) == 1:
                    cell_.set_num(pen[0])

    def fill_single(self, list_type):
        """
        fill list if pencil for a number only in one square
        if row does not contain 7
        check if duplicates in pencils for 7
        if no duplicates set_num(7)
        :return:
        """
        for i in range(9):
            # iterate through all rows/colums/boxes
            if list_type == 'row':
                cell_list = self.df.iloc[i]
            elif list_type == 'col':
                cell_list = self.df[i]
            else:
                cell_list = self.__dict__[f'_box{i}']

            # list of nums already in row/col/box
            list_str = [cell_list[j].get_num() for j in range(9)]
            for num in range(1,10):
                if num not in list_str:
                    pen_str = [cell_list[j].get_pencil() for j in range(9)]
                    pen_str = list(itertools.chain.from_iterable(pen_str))
                    if pen_str.count(num) == 1:
                        indx = self.find_pencil(num, i, list_type)[0]
                        cell = cell_list[indx]
                        print(f'{list_type} set cell {indx} to {num}')
                        cell.set_num(num)

    def xwing(self, list_type):
        """
        for rows 1,2,3:
            if pencils of cell in row x all in same box then remove pencils from rest of cells in box
        :param list_type:
        :return:
        """
        for i in range(3):
            if list_type == 'row':
                cell_list1 = self.df.iloc[i]
                cell_list2 = self.df.iloc[i+1]
                cell_list3 = self.df.iloc[i+2]
            elif list_type == 'col':
                cell_list1 = self.df[i]
                cell_list2 = self.df[i+1]
                cell_list3 = self.df[i+2]
            else:
                cell_list1 = self.__dict__[f'_box{i}']
                cell_list2 = self.__dict__[f'_box{i+1}']
                cell_list3 = self.__dict__[f'_box{i+2}']


    def solve_loop(self):
        # TODO change this to a while loop somehow
        self.create_boxes()
        self.fill_boxes()
        for i in range(0, 100):
            self.update_boxes()

            self.pencil_basic('row')
            self.pencil_basic('col')
            self.pencil_basic('box')

            self.fill_one_pencil()
            self.clear_pencils()

            self.fill_single('row')
            self.fill_single('col')
            self.fill_single('box')

            self.identify_pair('row')
            self.identify_pair('col')
            self.identify_pair('box')

    def check(self):
        errors = 0
        unsolved = 0
        # check columns
        for i in range(9):
            col = self.df[i]
            for j in range(9):
                val = col[j].get_num()
                if val == 0:
                    unsolved += 1
            errors += countDuplicate([col[j].get_num() for j in range(9)])
        # check rows
        for i in range(9):
            row = self.df.iloc[i]
            errors += countDuplicate([row[j].get_num() for j in range(9)])
        # check boxes
        for i in range(9):
            box = self.__dict__[f'_box{i}']
            errors += countDuplicate(box.get_nums())

        if errors == 0 and unsolved == 0:
            print("Puzzle Solved\n\n")
        else:
            print(f"{errors} errors, {unsolved} cells unsolved")

    def __str__(self):
        """
        :return: string of board with all knowns
        """
        print_vals = ''
        for i in range(9):
            print_cols = []
            for j in range(9):
                val = self.df.iloc[i][j].get_num()
                print_cols.append(val)
            print_vals += str(print_cols) + '\n'
        return str(print_vals)


def solve_puzzle(test):
    board = Grid(test)
    board.solve_loop()
    print(board)
    board.check()
    return board


def debug_cell(r, c):
    print(board.df.iloc[r][c].get_num())
    print(board.df.iloc[r][c].get_pencil())


# board =  solve_puzzle(debug1)
# board = solve_puzzle(test1)
# board = solve_puzzle(test2)
# board = solve_puzzle(test3)
# board = solve_puzzle(test4)
# board = solve_puzzle(test5)
board = solve_puzzle(test6)
# debug_cell(1,0)
debug_cell(0,3)
# board.fill_single('box')
# debug_cell(0,0)
# debug_cell(0,1)
# debug_cell(0,2)
# board.pairs_box()
# print(board)

# debug_cell(4,8)
# debug_cell(5,8)