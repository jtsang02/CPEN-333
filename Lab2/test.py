# using all()

winCombos = [[0, 1, 2], [1, 1, 1], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
for i in winCombos:
    if all(x == 1 for x in i):
        print("all 1s")
