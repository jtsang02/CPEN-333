#student name:      Josiah Tsang
#student number:    74191248 

import multiprocessing
from time import time

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    validColumn = set()
    for i in [c[column] for c in puzzle]:               # iterate thru values of column 'column' in puzzle
        if i in range(1,10): validColumn.add(i)         # add to set if conditions met
    print("Column", column, "valid" if len(validColumn) == 9 else "not valid") # check if set is 9

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    validRow = set()
    for i in puzzle[row]:                       # iterate thru values of row 'row' in puzzle
        if i in range(1,10): validRow.add(i)    # add to set if conditions met
    print("Row", row, "valid" if len(validRow) == 9 else "not valid") # check if set is 9

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    rowRange = [0,3] if subgrid < 3 else [3,6] if subgrid < 6 else [6,9]
    colRange = [0,3] if subgrid in [0,3,6] else [3,6] if subgrid in [1, 4, 7] else [6,9] 

    subList = set()
    for row in puzzle[rowRange[0]:rowRange[1]]:             # iterate thru rows
        for col in row[colRange[0]:colRange[1]]:            # iterate thru columns
            if col in range(1,10): subList.add(col)    
    print("Subgrid", subgrid, "valid" if len(subList) == 9 else "not valid") # check if set is 9

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

#array of processes
processes = []

tic = time()

for i in range(SIZE):  
    pSubgrid = multiprocessing.Process(target=checkSubgrid, args=(testcase, i))      #checking all subgrids
    pCol = multiprocessing.Process(target=checkColumn, args=(testcase, i))           #checking all columns
    pRow = multiprocessing.Process(target=checkRow, args=(testcase, i))              #checking all rows

    if __name__ == "__main__":
        pCol.start()
        processes.append(pCol)
        pRow.start()
        processes.append(pRow)
        pSubgrid.start()
        processes.append(pSubgrid)

# join all processes
for p in processes:
    p.join()

print("time=", time() - tic)