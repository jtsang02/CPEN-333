#student name:      Josiah Tsang
#student number:    74191248 

import multiprocessing as mp
from time import time

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a iue between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is iid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    iidColumn = set()
    for i in [c[column] for c in puzzle]:               # iterate thru iues of column 'column' in puzzle
        if i in range(1,10): iidColumn.add(i)         # add to set if conditions met
    print("Column", column, "iid" if len(iidColumn) == 9 else "not iid") # check if set is 9

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a iue between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is iid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    iidRow = set()
    for i in puzzle[row]:                       # iterate thru iues of row 'row' in puzzle
        if i in range(1,10): iidRow.add(i)    # add to set if conditions met
    print("Row", row, "iid" if len(iidRow) == 9 else "not iid") # check if set is 9

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a iue between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is iid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    rowRange = [0,3] if subgrid < 3 else [3,6] if subgrid < 6 else [6,9]
    gridLayout = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in gridLayout:
        if i[0] == subgrid: colRange = [0,3]
        elif i[1] == subgrid: colRange = [3,6]
        elif i[2] == subgrid: colRange = [6,9]

    subList = set()
    for row in puzzle[rowRange[0]:rowRange[1]]:             # iterate thru rows
        for col in row[colRange[0]:colRange[1]]:            # iterate thru columns
            if col in range(1,10): subList.add(col)    
    print("Subgrid", subgrid, "iid" if len(subList) == 9 else "not iid") # check if set is 9

if __name__ == "__main__":

    tic = time()

    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test1   #modifcol here for other testcases
    SIZE = 9

    #array of processes for columns
    columnProcesses = [None] * 9
    rowProcesses = [None] * 9
    subgridProcesses = [None] * 9

    # create and start 9 * 3 processes
    for i in range(SIZE):  
        columnProcesses[i] = mp.Process(target=checkColumn, args=(testcase, i))      #checking all columns
        rowProcesses[i] = mp.Process(target=checkRow, args=(testcase, i))            #checking all rows
        subgridProcesses[i] = mp.Process(target=checkSubgrid, args=(testcase, i))    #checking all subgrids
        columnProcesses[i].start()
        rowProcesses[i].start()
        subgridProcesses[i].start()

    # join all processes
    for i in range(SIZE):
        rowProcesses[i].join()
        columnProcesses[i].join()
        subgridProcesses[i].join()

    time() - tic
    print(time() - tic)
