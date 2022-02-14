#student name:      Josiah Tsang
#student number:    74191248

import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    tempList = testcase
    midIndex = len(tempList) // 2
        
    if firstHalf:
        # sort first half and store it in sortedFirstHalf   
        tempList = tempList[:midIndex]
    else:
        # sort second half and store it in sortedSecondHalf
        tempList = tempList[midIndex:]
    
    # sort tempList and store into appropriate variable

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """

    pass #to Implement

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 
    # use threading here
    
    sortingWorker(True)

    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)

    # https://www.geeksforgeeks.org/merge-sort/