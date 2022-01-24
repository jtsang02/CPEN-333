# student name:     Josiah Tsang
# student number:   74191248
def displayPyramid(size: int) -> None:
    """
        This method prints a pyramid of size size.
        Implement the method using nested for loops.
        size is an integer between 1 and 9 (inclusive).
        Example: if size is 7, it should print:
            1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
  6 5 4 3 2 1 2 3 4 5 6
7 6 5 4 3 2 1 2 3 4 5 6 7
    """
    
    for i in range(1, size + 1):        # iterate thru number of triangles
        # 3 inner loops
        j = 1
        while j < size - i + 1:         # first inner loop print front spaces
            print(end=" ")
            j += 1
        k = i
        while k > 0:                    # second inner loop prints left side of triangle 
            print(k, end=" ")
            k -= 1
        m = 2
        while m < i + 1:                # third inner loop prints right side of triangle
            print(m, end=" ")
            m += 1
        print("")                       

    pass  # remove this line, it is here for now for the code to be valid


if __name__ == "__main__":
    """ 
        We will ignore this part of the code.
        You can use it to test your function.
        Make sure that you fully test your code.
        This prints the output for all rquired 
        sizes, from 1 to 9.
    """
    for size in range(1, 10):
        displayPyramid(size)
