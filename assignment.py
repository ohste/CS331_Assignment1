
#!/usr/bin/python
import sys
import math
import csv

#Generic file handling function to read the two state files
def fileStuff(filepath):
    f = open(filepath,"r")
    reader = csv.reader(f)
    left = next(reader)
    leftBank = [int(left[0]), int(left[1]), int(left[2])]
    right = next(reader)
    rightBank = [int(right[0]), int(right[1]), int(right[2])]
    f.close()
    return leftBank, rightBank

#Gets the initial and final states and stores them in named variables
def entry():
    initialLeft, initialRight = fileStuff(sys.argv[1])
    initialState = [initialLeft, initialRight]
    finalLeft, finalRight = fileStuff(sys.argv[2])
    finalState = [finalLeft, finalRight]
    outputFile = sys.argv[4]
    return initialState, finalState, outputFile

def bfs(initialState, finalState, outputFile):
    print("Running bfs...")

def dfs(initialState, finalState, outputFile):
    print("Running dfs...")

def iddfs(initialState, finalState, outputFile):
    print("Running iddfs...")

def astar(initialState, finalState, outputFile):
    print("Running astar...")


if __name__ == '__main__':

    if(len(sys.argv) != 5):
        print("Err: Missing arguments")
        quit()
    #Here we will parse the files to get the proper input
    initialState, finalState, outputFile = entry()

    #Here we get the mode that we want to run each number represents an algorithm
    # 1 = bfs (breadth first search)
    # 2 = dfs (depth first search)
    # 3 = iddfs (for iterative deepening depth-first search)
    # 4 = astar (A-Star search)

    algo_mode = sys.argv[3]

    if algo_mode == "1":
        bfs(initialState, finalState, outputFile)
    elif algo_mode == "2":
        dfs(initialState, finalState, outputFile)
    elif algo_mode == "3":
        iddfs(initialState, finalState, outputFile)
    elif algo_mode == "4":
        astar(initialState, finalState, outputFile)
    else:
        print("Invalid Mode")
