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
    def sort(listToSort : list) -> None:                # inner function to sort half the list using insertion sort algorithm
        for i in range(len(listToSort)):                # iterate thru list   
            current = listToSort[i]                     # store current item in temp var
            j = i - 1                                   # loop variable of sorted items (start from previous item)
            while (j >= 0 and listToSort[j] > current): # iterate thru sorted items
                listToSort[j + 1] = listToSort[j]       # copy item to the right 
                j -= 1                                  # decrement loop variable
            listToSort[j + 1] = current                 # after while loop, all greater items shifted to right, store current item

    tempList = testcase                                 # copy testcase to new list        
    midIndex = len(tempList) // 2                       # get midpoint index of list
        
    if firstHalf:
        tempList = tempList[:midIndex]                  # sort first half and store it in sortedFirstHalf                                                   # get first half of list 
    else:         
        tempList = tempList[midIndex:]                  # sort second half and store it in sortedSecondHalf   
    
    sort(tempList)                                      # call inner function to sort half of list                        

    for item in tempList:                               
        if firstHalf:                                   # add to appropriate shared variable
            sortedFirstHalf.append(item)      
        else:
            sortedSecondHalf.append(item)
            
    # print(f" {str(tempList)} from thread {threading.current_thread().name}")

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    i = j = 0                                           # set loop variables to 0
    size = len(sortedFirstHalf)                         # size is len of half array
    
    while i < size and j < size:                        # traverse both lists before running out of values to compare on one list
        if sortedFirstHalf[i] < sortedSecondHalf[j]:    # compare two values of list    
            SortedFullList.append(sortedFirstHalf[i])   # if value in the firsthalf list is less, add to fullsorted list
            i += 1                                      # move on to the next value in the firsthalf list
        else:                                           
            SortedFullList.append(sortedSecondHalf[j])  # otherwise value of secondhalf list is smaller, add this value to full sorted list
            j += 1                                      # move on to the next value in the secondhalf list

    for item in sortedFirstHalf[i:]:                    # if items left in firstHalf, add to fullsorted list
        SortedFullList.append(item)
    for item in sortedSecondHalf[j:]:                   # otherewise add leftover items in secondhalf to fullsorted list
        SortedFullList.append(item)
    
    # print(f" {str(SortedFullList)} from thread {threading.current_thread().name}")

if __name__ == "__main__":
    #shared variables
    testcase1 = [8,5,7,7,4,1,3,2]
    testcase2 = [7, 3, 3, 2, 3, 1, 5, 8]
    testcase3 = [7, -1, 3, 2, 1, 1, -5, 4]
    testcase4 = []
    testcase5 = [0]
    testcase6 = [-5, 4, 2, -9]
    testcase = testcase1
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 
    # use threading here
    t1 = threading.Thread(target = sortingWorker, kwargs={"firstHalf": True})
    t2 = threading.Thread(target = sortingWorker, kwargs={"firstHalf": False})
    t3 = threading.Thread(target = mergingWorker)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3.start()
    t3.join()

    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)