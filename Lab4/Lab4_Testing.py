#student name:      Josiah Tsang
#student number:    74191248

import threading
import unittest

class TestLab4:

    testcase: list = []
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    sortedFullList: list = []

    def __init__(self, passedList: list):
        #shared variables
        self.testcase = passedList
        TestLab4.sortedFirstHalf.clear()
        TestLab4.sortedSecondHalf.clear()
        TestLab4.sortedFullList.clear()
    
    def sortingWorker(self, firstHalf: bool) -> None:
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

        tempList = self.testcase                            # copy testcase to new list        
        midIndex = len(tempList) // 2                       # get midpoint index of list
            
        if firstHalf:
            tempList = tempList[:midIndex]                  # sort first half and store it in sortedFirstHalf                                                   # get first half of list 
        else:         
            tempList = tempList[midIndex:]                  # sort second half and store it in sortedSecondHalf   
        
        sort(tempList)                                      # call inner function to sort half of list                        

        for item in tempList:                               
            if firstHalf:                                   # add to appropriate shared variable
                TestLab4.sortedFirstHalf.append(item)      
            else:
                TestLab4.sortedSecondHalf.append(item)
        # print(f" {str(tempList)} from thread {threading.current_thread().name}")

    def mergingWorker(self) -> None:
        """ This function uses the two shared variables 
            sortedFirstHalf and sortedSecondHalf, and merges
            them into a single sorted list that is stored in
            the shared variable sortedFullList.
        """
        i = j = 0                                                               # set loop variables to 0
        size = len(TestLab4.sortedFirstHalf)                                    # size is len of half array
        
        while i < size and j < size:                                            # traverse both lists before running out of values to compare on one list
            if TestLab4.sortedFirstHalf[i] < TestLab4.sortedSecondHalf[j]:      # compare two values of list    
                TestLab4.sortedFullList.append(TestLab4.sortedFirstHalf[i])     # if value in the firsthalf list is less, add to fullsorted list
                i += 1                                                          # move on to the next value in the firsthalf list
            else:                                           
                TestLab4.sortedFullList.append(TestLab4.sortedSecondHalf[j])    # otherwise value of secondhalf list is smaller, add this value to full sorted list
                j += 1                                                          # move on to the next value in the secondhalf list

        for item in TestLab4.sortedFirstHalf[i:]:                               # if items left in firstHalf, add to fullsorted list
            TestLab4.sortedFullList.append(item)
        for item in self.sortedSecondHalf[j:]:                                  # otherewise add leftover items in secondhalf to fullsorted list
            TestLab4.sortedFullList.append(item)
        
    def testFunction(self) -> list:
        """ function to unit test 
        """
        t1 = threading.Thread(target = self.sortingWorker, kwargs={"firstHalf": True})
        t2 = threading.Thread(target = self.sortingWorker, kwargs={"firstHalf": False})
        t3 = threading.Thread(target = self.mergingWorker)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        t3.start()
        t3.join()
        return TestLab4.sortedFullList                

class unitTest(unittest.TestCase):      
    
    # write unit tests here
    
    def test1(self):
        testCase1 = [7, -1, 3, 2]
        newTest = TestLab4(testCase1)
        self.assertListEqual(sorted(testCase1), newTest.testFunction())

    def test2(self):
        testCase2 = [7, 3, 3, 2, 3, 1, 5, 8]
        newTest2 = TestLab4(testCase2)
        self.assertListEqual(sorted(testCase2), newTest2.testFunction())

    def test3(self):
        testCase3 = [7, -1, 3, 2, 1, 1, -5, 4]
        newTest3 = TestLab4(testCase3)
        self.assertListEqual(sorted(testCase3), newTest3.testFunction())

    def test4(self):
        testCase4 = ['a', 'b', 'd', 'c']
        newTest = TestLab4(testCase4)
        self.assertListEqual(sorted(testCase4), newTest.testFunction())

if __name__ == '__main__':
    unittest.main()
