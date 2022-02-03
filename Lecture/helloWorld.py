import math


# even = False
# if even:
#     print("It is even!")

# #print(math.sqrt(math.sin(math.pi + 1) ** 2))


# # Python
# for i in range(3):
#     print(i)

def main():
    myCount = Count()
    times = 0

    for i in range(0, 100):
        increment(myCount, times)
    
    print("count is", myCount.count, "and times is", times)

def increment(c, times):
    c.count += 1
    times += 1

class Count:
    def __init__(self):
        self.count = 0
    
if __name__ == "__main__":
    main()