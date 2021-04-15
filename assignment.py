
#!/usr/bin/python
import sys
import math
import csv

def fileStuff(filepath):
    f = open(filepath,"r")
    reader = csv.reader(f)
    left = next(reader)
    leftBank = [int(left[0]), int(left[1]), int(left[2])]
    right = next(reader)
    rightBank = [int(right[0]), int(right[1]), int(right[2])]
    f.close()
    return leftBank, rightBank

def entry():
    initialLeft, initialRight = fileStuff(sys.argv[1])
    print("Left Bank", initialLeft)
    print("Right Bank", initialRight)
    finalLeft, finalRight = fileStuff(sys.argv[2])
    print("Left Bank", finalLeft)
    print("Right Bank", finalRight)
    algToUse = sys.argv[3]
    outputFile = sys.argv[4]

def bfs():
    print("Running bfs...")

def dfs():
    print("Running dfs...")   

def iddfs():
    print("Running iddfs...")

def astar():
    print("Running astar...")


if __name__ == '__main__':

    #Here we will parse the files to get the proper input


    #Here we get the mode that we want to run each number represents an algorithm
    # 1 = bfs (breadth first search)
    # 2 = dfs (depth first search)
    # 3 = iddfs (for iterative deepening depth-first search)
    # 4 = astar (A-Star search)

    algo_mode = sys.argv[3]

    if algo_mode == "1":
        bfs()
    elif algo_mode == "2":
        dfs()
    elif algo_mode == "3":
        iddfs()
    elif algo_mode == "4":
        astar()
    else:
        print("Invalid Mode")



